#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Default: the FLUX.2 Klein 4B model, used here as an image editor.
# A Hugging Face repo id, resolved by MLX-Gen (mflux) from the local HF cache
# (or downloaded on demand). Override with --model for a local model directory.
DEFAULT_MODEL_DIR: str = "black-forest-labs/FLUX.2-klein-4B"
# Logical model name understood by mflux's ModelConfig.from_name / flux2_klein_4b().
DEFAULT_MODEL_NAME: str = "flux2-klein-4b"
# FLUX.2 Klein 4B is a turbo variant: mflux default is 4 steps.
DEFAULT_STEPS: int = 4
DEFAULT_SEED: int = 1928374650
# FLUX.2 uses guidance 1.0 for edits and 4.0 for masked inpaint.
DEFAULT_EDIT_GUIDANCE: float = 1.0
DEFAULT_INPAINT_GUIDANCE: float = 4.0
DEFAULT_OUTPUT: Path = Path("./test/tmp/flux-edit.jpg")
# Local directory must contain these subfolders to be treated as a complete model.
REQUIRED_MODEL_SUBDIRS: tuple[str, ...] = ("text_encoder", "tokenizer", "transformer", "vae")


def bounded_integer(option: str, minimum: int, maximum: int | None = None) -> "callable":
    def checker(value: str) -> int:
        try:
            parsed = int(value)
        except ValueError:
            raise argparse.ArgumentTypeError(f"{option} must be an integer, got '{value}'.")
        if parsed < minimum:
            raise argparse.ArgumentTypeError(f"{option} must be >= {minimum}, got {parsed}.")
        if maximum is not None and parsed > maximum:
            raise argparse.ArgumentTypeError(f"{option} must be <= {maximum}, got {parsed}.")
        return parsed

    return checker


def non_empty_text(option: str) -> "callable":
    def checker(value: str) -> str:
        if not value or not value.strip():
            raise argparse.ArgumentTypeError(f"{option} must be non-empty.")
        return value

    return checker


def optional_float(option: str) -> "callable":
    def checker(value: str) -> float:
        try:
            parsed = float(value)
        except ValueError:
            raise argparse.ArgumentTypeError(f"{option} must be a number, got '{value}'.")
        return parsed

    return checker


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="flux-edit",
        description="Edit or inpaint an image with the FLUX.2 Klein 4B model via MLX-Gen (mflux).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog=(
            "Without --mask the image is edited globally (Flux2KleinEdit). With --mask "
            "only the masked (white) area is repainted, e.g. to remove people "
            "(Flux2KleinInpaint)."
        ),
    )
    parser.add_argument(
        "--model",
        type=non_empty_text("--model"),
        default=DEFAULT_MODEL_DIR,
        help="Hugging Face repo id (default) or local model directory for FLUX.2 Klein.",
    )
    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help="Source image to edit or inpaint (PNG/JPG).",
    )
    parser.add_argument(
        "--mask",
        type=Path,
        default=None,
        help="Optional mask image. White = repaint, black = preserve. Enables inpaint mode.",
    )
    parser.add_argument(
        "--prompt",
        type=non_empty_text("--prompt"),
        required=True,
        help="Text describing the desired result, e.g. 'empty museum hall, no people, clean floor'.",
    )
    parser.add_argument(
        "--width",
        type=bounded_integer("--width", 1, 8192),
        default=None,
        help="Output width in pixels. Defaults to the source aspect ratio.",
    )
    parser.add_argument(
        "--height",
        type=bounded_integer("--height", 1, 8192),
        default=None,
        help="Output height in pixels. Defaults to the source aspect ratio.",
    )
    parser.add_argument(
        "--steps",
        type=bounded_integer("--steps", 1, 1000),
        default=DEFAULT_STEPS,
        help="Number of inference steps (FLUX.2 Klein 4B is a turbo model, 4 works well).",
    )
    parser.add_argument(
        "--seed",
        type=bounded_integer("--seed", 0, 2**32 - 1),
        default=DEFAULT_SEED,
        help="Random seed for reproducibility.",
    )
    parser.add_argument(
        "--guidance",
        type=optional_float("--guidance"),
        default=None,
        help="Guidance scale. Defaults to 1.0 for edit mode and 4.0 for masked inpaint.",
    )
    parser.add_argument(
        "--image-strength",
        type=optional_float("--image-strength"),
        default=None,
        help="How strongly the source image influences the edit (0.0-1.0). Edit mode only.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output image path (.png, .jpg, .jpeg).",
    )
    return parser


def validate_input(parser: argparse.ArgumentParser, value: Path) -> Path:
    if not value.exists():
        parser.error(f"Input file not found: {value}")
    if value.is_dir():
        parser.error(f"Input must be a file, not a directory: {value}")
    return value


def validate_mask(parser: argparse.ArgumentParser, value: Path | None) -> Path | None:
    if value is None:
        return None
    if not value.exists():
        parser.error(f"Mask file not found: {value}")
    if value.is_dir():
        parser.error(f"Mask must be a file, not a directory: {value}")
    return value


def validate_model(parser: argparse.ArgumentParser, value: str) -> str:
    """Validate the model reference.

    A local model directory must contain the expected subfolders. A value that is
    not a local directory (e.g. a Hugging Face repo id) is passed through to mflux,
    which resolves it from the HF cache or downloads it on demand.
    """
    resolved = Path(value).expanduser()
    if resolved.is_dir():
        missing = [name for name in REQUIRED_MODEL_SUBDIRS if not (resolved / name).is_dir()]
        if missing:
            parser.error(f"Model directory is incomplete at '{resolved}'. Missing subdirectories: {', '.join(missing)}")
    return value


def validate_output(parser: argparse.ArgumentParser, output: Path) -> Path:
    parent = output.parent
    if output.is_dir():
        parser.error(f"Output path must be a file, not a directory: {output}")
    suffix = output.suffix.lower()
    if suffix not in {".png", ".jpg", ".jpeg"}:
        parser.error(f"Output must be a .png, .jpg, or .jpeg file, got '{suffix or '(none)'}'")
    if not parent.exists():
        parser.error(f"Output parent directory does not exist: {parent}")
    return output


def generate(args: argparse.Namespace) -> Path:
    from mflux.models.common.config import ModelConfig
    from mflux.models.flux2.variants import Flux2KleinEdit
    from mflux.models.flux2.variants.edit.flux2_klein_inpaint import Flux2KleinInpaint

    model_config = ModelConfig.from_name(model_name=DEFAULT_MODEL_NAME)

    if args.mask is not None:
        guidance = args.guidance if args.guidance is not None else DEFAULT_INPAINT_GUIDANCE
    else:
        guidance = args.guidance if args.guidance is not None else DEFAULT_EDIT_GUIDANCE

    if args.mask is not None:
        # Masked inpaint: repaint only the white (masked) region, e.g. remove people.
        model = Flux2KleinInpaint(model_path=str(args.model), model_config=model_config)
        image = model.generate_image(
            seed=args.seed,
            prompt=args.prompt,
            image_path=args.input,
            mask_path=args.mask,
            num_inference_steps=args.steps,
            height=args.height,
            width=args.width,
            guidance=guidance,
        )
    else:
        # Global edit: the whole image is conditioned by the source.
        model = Flux2KleinEdit(model_path=str(args.model), model_config=model_config)
        image = model.generate_image(
            seed=args.seed,
            prompt=args.prompt,
            image_paths=[args.input],
            num_inference_steps=args.steps,
            height=args.height,
            width=args.width,
            guidance=guidance,
            image_strength=args.image_strength,
        )

    image.save(path=args.output, overwrite=False)
    return args.output


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    validate_input(parser, args.input)
    args.mask = validate_mask(parser, args.mask)
    args.model = validate_model(parser, args.model)
    validate_output(parser, args.output)
    if args.mask is not None and args.image_strength is not None:
        parser.error("--image-strength is only valid in edit mode (without --mask).")

    try:
        generate(args)
    except (OSError, RuntimeError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Immagine modificata salvata in: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
