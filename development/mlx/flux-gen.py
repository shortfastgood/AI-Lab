#!/usr/bin/env python3
"""Generate an image programmatically with the MLX-Gen Python API."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Default model: FLUX.2 Klein 4B, a Hugging Face repo id resolved by MLX-Gen
# (mflux) from the local HF cache (or downloaded on demand).
DEFAULT_MODEL = "black-forest-labs/FLUX.2-klein-4B"
DEFAULT_WIDTH = 1280
DEFAULT_HEIGHT = 1024
DEFAULT_STEPS = 4
DEFAULT_SEED = 192837465
DEFAULT_OUTPUT = Path("./test/tmp/output.png")


def bounded_integer(option: str, minimum: int, maximum: int | None = None):
    def parse(value: str) -> int:
        try:
            number = int(value)
        except ValueError:
            raise argparse.ArgumentTypeError(
                f"{option} must be an integer; received: {value!r}"
             ) from None

        if number < minimum:
            raise argparse.ArgumentTypeError(
                f"{option} must be greater than or equal to {minimum}; received: {number}"
             )
        if maximum is not None and number >= maximum:
            raise argparse.ArgumentTypeError(
                f"{option} must be less than {maximum}; received: {number}"
             )
        return number

    return parse


def non_empty_text(option: str):
    def parse(value: str) -> str:
        if not value.strip():
            raise argparse.ArgumentTypeError(f"{option} cannot be empty")
        return value

    return parse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
              "Generate an image using the MLX-Gen Python API directly, "
              "without running the mlxgen command."
          )
      )
    parser.add_argument(
           "--model",
        type=non_empty_text("--model"),
        default=DEFAULT_MODEL,
        help=f"MLX-Gen text-to-image model (default: {DEFAULT_MODEL}).",
       )
    parser.add_argument(
           "--prompt",
        required=True,
        type=non_empty_text("--prompt"),
        help="Description of the image to generate.",
       )
    parser.add_argument(
           "--width",
        type=bounded_integer("--width", minimum=1, maximum=10_000),
        default=DEFAULT_WIDTH,
        help=f"Width in pixels (default: {DEFAULT_WIDTH}; range: 1-9999).",
       )
    parser.add_argument(
           "--height",
        type=bounded_integer("--height", minimum=1, maximum=10_000),
        default=DEFAULT_HEIGHT,
        help=f"Height in pixels (default: {DEFAULT_HEIGHT}; range: 1-9999).",
       )
    parser.add_argument(
           "--steps",
        type=bounded_integer("--steps", minimum=1, maximum=100),
        default=DEFAULT_STEPS,
        help=f"Number of steps (default: {DEFAULT_STEPS}; range: 1-99).",
       )
    parser.add_argument(
           "--seed",
        type=bounded_integer("--seed", minimum=1),
        default=DEFAULT_SEED,
        help=f"Positive seed (default: {DEFAULT_SEED}).",
       )
    parser.add_argument(
           "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Destination image file (default: {DEFAULT_OUTPUT}).",
        )
    return parser


def validate_model(parser: argparse.ArgumentParser, value: str) -> str:
    """Validate the model reference.
    A local directory must contain the expected subdirectories. A value that
    is not a local directory (e.g. a Hugging Face repo id) is passed to mflux,
    which resolves it from the HF cache or downloads it on demand.
    """
    resolved = Path(value).expanduser()
    if resolved.is_dir():
        required_entries = ("text_encoder", "tokenizer", "transformer", "vae")
        missing = [entry for entry in required_entries if not (resolved / entry).is_dir()]
        if missing:
            parser.error(
                f"--model is not a complete MLX-Gen model; missing: {', '.join(missing)}"
              )

    return value


def validate_output(parser: argparse.ArgumentParser, output: Path) -> Path:
    output = output.expanduser()
    if output.exists() and output.is_dir():
        parser.error(f"--output must point to a file, not a directory: {output}")
    if output.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
        parser.error("--output must have a .png, .jpg, or .jpeg extension")
    if output.parent.exists() and not output.parent.is_dir():
        parser.error(f"The parent directory of --output is not valid: {output.parent}")
    return output


def generate(args: argparse.Namespace) -> Path:
    try:
        from mflux.models.common.config import ModelConfig
        from mflux.models.flux2.variants.txt2img.flux2_klein import Flux2Klein
    except ImportError as exc:
        raise RuntimeError(
             "MLX-Gen is not installed. Run: "
             "python3 -m pip install -r development/python/requirements.txt"
         ) from exc

    print(f"Loading model: {args.model}", flush=True)
    model_config = ModelConfig.flux2_klein_4b()

    model = Flux2Klein(
        model_path=str(args.model),
        model_config=model_config,
       )

    print(
        f"Generating {args.width}x{args.height}, {args.steps} steps, seed {args.seed}...",
        flush=True,
    )
    image = model.generate_image(
        seed=args.seed,
        prompt=args.prompt,
        width=args.width,
        height=args.height,
        num_inference_steps=args.steps,
    )
    return image.save(path=args.output, overwrite=False)


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    args.model = validate_model(parser, args.model)
    args.output = validate_output(parser, args.output)

    try:
        saved_path = generate(args)
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Image saved to: {saved_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
