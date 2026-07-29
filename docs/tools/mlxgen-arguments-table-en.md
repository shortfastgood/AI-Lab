# MLX-Gen Arguments Table (MLX Framework - Apple)

**Program:** `mlxgen` (MLX-Gen CLI)  
**Version:** 0.25.0 (2026-07-25)  
**Main subcommands:** `generate`, `upscale`, `capabilities`, `validation`, `download`, `prepare`

---

## Arguments Table by Subcommand

### 1. `mlxgen generate` Command

Generates images or videos, and edits images, from a prepared or cached model.

| Argument | Description | Possible Values / Examples |
|----------|-------------|---------------------------|
| `--model`, `-m` **MODEL** | Model alias, Hugging Face repo, or local model path. | `z-image-turbo`, `wan2.2-ti2v-5b`, `flux2-klein-4b`, or a local path such as `./models/qwen-image` |
| `--base-model` **BASE_MODEL** | Base model hint for custom repositories or local paths. | Any valid model alias |
| `--family` **{qwen, flux2, fibo, z-image, ernie-image, wan, bonsai}** | Override automatic family detection for the model. Use for local paths or custom repo names. | `qwen`, `flux2`, `fibo`, `z-image`, `ernie-image`, `wan`, `bonsai` |
| `--debug` | Enables debug logging for internal generation details (e.g. LoRA fusion targets). | Boolean flag, no value required |
| `--task` **{auto, text-to-image, txt2img, image-to-image, img2img, edit, text-to-video, txt2vid, t2v, image-to-video, img2vid, i2v, video-to-video, vid2vid, v2v}** | Overrides automatic routing. Default: auto. | `auto`, `text-to-image` (`txt2img`), `image-to-image` (`img2img`), `edit`, `text-to-video` (`txt2vid`, `t2v`), `image-to-video` (`img2vid`, `i2v`), `video-to-video` (`vid2vid`, `v2v`) |
| `--i2i-mode` **{auto, latent, img2img, edit, edit-reference, multi, multi-reference}** | Internal image-to-image mode. Default: auto. Use `latent/img2img` for image-strength variation, `edit` for instruction/reference-based edits, or `multi-reference` for two or more input images. | `auto`, `latent`, `img2img`, `edit`, `edit-reference`, `multi`, `multi-reference` |
| `--image`, `--input-image`, `-i` **IMAGES** | Input image. Use one image for image-to-image or Wan first-frame image-to-video. Repeat only for multi-reference image-to-image. | Image file path: `.png`, `.jpg`, etc. |
| `--images`, `--input-images`, `--image-paths` **IMAGE_GROUPS [...]** | One or more input images for image-to-image reference/edit modes. | List of image file paths |
| `--image-path` **IMAGE_PATH** | Compatibility alias for a single input image, including Wan first-frame image-to-video. | Image file path |
| `--video`, `--input-video` **VIDEOS** | Source video for plain prompt-guided video-to-video routes. | Video file path: `.mp4`, etc. |
| `--video-path` **VIDEO_PATH** | Compatibility alias for a single source video on plain video-to-video routes. | Video file path |
| `--video-strength` **VIDEO_STRENGTH** | Denoising strength for plain video-to-video routes. Higher values allow greater appearance changes. | Decimal number (e.g. `0.5`, `0.8`) |
| `--video-mask-path` **VIDEO_MASK_PATH** | Static image mask for masked video-to-video. White marks the region the model may change; black regions are preserved exactly from the source video. | Image mask file path (PNG) |
| `--reframe-padding` **REFRAME_PADDING** | Generative reframe request: CSS-style `top,right,bottom,left` padding. Edit models redraw into the larger canvas; this is not masked outpainting and does not preserve source pixels exactly. | CSS-style: `0,25%,0,25%`, `10px,10px,10px,10px` |
| `--outpaint-padding`, `--image-outpaint-padding` **OUTPAINT_PADDING** | Canvas outpaint request: CSS-style `top,right,bottom,left` padding. Qwen Image Edit uses generative canvas expansion with adaptive source restoration. FLUX.2 strict outpaint requires a base Klein model and uses source-locked denoising instead of generative reframe. | CSS-style: `0,25%,0,25%`, `50px,50px,50px,50px` |

#### Common Generation Options (forwarded to the selected backend)

| Argument | Description | Possible Values / Examples |
|----------|-------------|---------------------------|
| `--prompt` | Textual prompt describing the image/video to generate. | Free text string: `"A puffin standing on a cliff"` |
| `--prompt-file` | Reads the prompt from a file. | File path `.txt` |
| `--width` | Output width in pixels. | Integer (e.g. `1024`, `1280`) |
| `--height` | Output height in pixels. | Integer (e.g. `768`, `1024`) |
| `--steps` | Number of diffusion steps. | Integer (e.g. `30`, `50`) |
| `--guidance` | Guidance scale for prompt control. | Decimal number (e.g. `7.5`, `9.0`) |
| `--seed` | Entropy seed for reproducibility. | Positive integer (e.g. `42`) |
| `--auto-seeds` | Auto-generates N entropy seeds (random integers between 0 and 10,000,000). | Integer (e.g. `5` = generates 5 random seeds) |
| `--negative-prompt`, `--negative` | Negative prompt to exclude elements from the output. | Free text string: `"blurry, low quality"` |
| `--canvas-policy` | Canvas management policy. | Backend-specific value |
| `--resize-mode` | Resize mode (latent image-to-image and Wan video routes). | Backend-specific value |
| `--quantize` | Model quantisation. | `3`, `4`, `5`, `6`, `8` bits |
| `--lora-paths` | LoRA paths: local files, HuggingFace repos (org/model), or collection format (repo:filename.safetensors). | List of paths or repo IDs |
| `--lora-scales` | Scaling factor to adjust the impact of LoRA weights on the model. A value of `1.0` applies the LoRA weights as they are. | List of decimals (e.g. `1.0`, `0.8`) |
| `--mask-path` | Mask path for localised edit or inpaint on models that support masked edit/inpaint. | Image mask file path (PNG) |
| `--controlnet-image-path` | ControlNet image path for structured control on a text-to-image route. Not the same as source-image editing. | Image file path |
| `--controlnet-strength` | ControlNet strength. | Decimal number (e.g. `0.8`) |
| `--metadata` | Exports image metadata as a JSON file. | Boolean flag |
| `--embed-metadata` | Embeds metadata into the saved image file. Default: off. | Boolean flag |
| `-C`, `--config-from-metadata` | Configures from existing metadata. | Boolean flag |
| `--output` | Filename for the output image/video. Supports `{seed}` and `{input_name}` when processing several source files. Default: `"image.png"`. | String: `"result.png"`, `"video_{seed}.mp4"` |
| `--replace` | Replaces existing output file if it exists. | Boolean flag |
| `--frames` | Number of frames for video. | Integer |
| `--fps` | Frames per second for video. | Integer (e.g. `24`, `30`) |
| `--guidance-2` | Second guidance scale. | Decimal number |
| `--flow-shift` | Flow shift parameter. | Decimal number |
| `--low-ram` | Enables low-RAM mode to reduce memory usage (may impact performance). | Boolean flag |
| `--tensor-health-check-interval` | Interval for tensor health checks. | Integer (ms) |
| `--json-events` | Emits machine-readable JSONL events to stdout, CLI text to stderr. | Boolean flag |
| `--keep-text-encoder` | Keeps text encoder in memory. | Boolean flag |
| `--no-prompt-cache` | Disables prompt caching. | Boolean flag |
| `--compile-transformer` | Compiles transformer for performance. | Boolean flag |
| `--release-inactive-denoiser`, `--no-release-inactive-denoiser` | Releases inactive denoiser (Wan routes). | Boolean flag |
| `--progress`, `--no-progress` | Shows/disables CLI progress. Default: true. | Boolean flag |

---

### 2. `mlxgen upscale` Command

Restores or upscales images and videos with SeedVR2 diffusion-based super-resolution.

| Argument | Description | Possible Values / Examples |
|----------|-------------|---------------------------|
| `--battery-percentage-stop-limit`, `-B` **BATTERY_PERCENTAGE_STOP_LIMIT** | On Macs running on battery, stops image generation when the battery reaches this percentage. Default: 5 | Integer (e.g. `5`, `10`) |
| `--low-ram` | Enables low-RAM mode to reduce memory usage. | Boolean flag |
| `--mlx-cache-limit-gb` **MLX_CACHE_LIMIT_GB** | Limits MLX cache size in GB without enabling full low-RAM mode. Default: machine-derived (total RAM / 8, clamped 1-8 GiB). `-1` = unlimited. | Integer or `-1`: `8`, `16`, `-1` |
| `--debug` | Enables debug logging for internal details. | Boolean flag |
| `--json-events` | Emits machine-readable JSONL events to stdout. | Boolean flag |
| `--progress`, `--no-progress` | Shows/disables CLI progress. Default: true. | Boolean flag |
| `--model`, `-m` **MODEL** | SeedVR2 model alias (official HF repo, AbstractFramework SeedVR2 package, or local path). | `seedvr2`, `seedvr2-3b`, `seedvr2-7b`, `seedvr2-7b-sharp` |
| `--base-model` **BASE_MODEL** | Base model alias or upstream repo ID for prepared/custom checkpoints. | Any valid model alias |
| `--quantize`, `-q` **{3, 5, 4, 6, 8}** | Quantises the model. Default: None. | `3`, `4`, `5`, `6`, `8` bits |
| `--metadata` | Exports image metadata as a JSON file. | Boolean flag |
| `--embed-metadata` | Embeds metadata into the saved image file. Default: off. | Boolean flag |
| `--output` **OUTPUT** | Filename for the output image/video. Supports `{seed}` and `{input_name}`. Default: `"image.png"`. | String: `"upscaled.png"` |
| `--replace [REPLACE]` | Replaces the target output file when it already exists. Use `--replace false` or `--no-replace` to keep the existing file and save to a suffixed path. | Flag with optional value: `true`, `false` |
| `--no-replace` | Does not replace an existing output file; saves to the next suffixed filename instead. | Boolean flag |
| `--stepwise-image-output-dir` **[EXPERIMENTAL]** | Output directory for step-wise images and their final composite image. This feature may change in future versions. | Directory path |

#### SeedVR2 Upscale Configuration

| Argument | Description | Possible Values / Examples |
|----------|-------------|---------------------------|
| `--image-path`, `-i` **IMAGE_PATH [...]** | Path to input image(s) or directories to upscale. | List of `.png`, `.jpg` paths or directories |
| `--video-path` **VIDEO_PATH [...]** | Path to input video(s) or directories to restore/upscale. | List of `.mp4` paths or directories |
| `--seed`, `-s` **SEED [...]** | Specify 1+ Entropy Seeds. Default: 1 time-based random seed. | List of integers: `42`, `123`, `456` |
| `--auto-seeds` **AUTO_SEEDS** | Auto-generates N entropy seeds (random integers between 0 and 10,000,000). | Integer (e.g. `5` = generates 5 seeds) |
| `--resolution`, `-r` **RESOLUTION** | Target resolution for the shortest edge (pixels) or scale factor (e.g. `'2x'`). For video, omitting `--resolution` defaults to `1x`. | Scale: `2x`, `3x`; or pixels: `1024`, `2048` |
| `--softness` **SOFTNESS** | Value between 0.0 (off, factor 1) and 1.0 (max, factor 8). Default: 0.0. | Decimal: `0.0`, `0.5`, `1.0` |
| `--color-correction` **{wavelet, lab, off}** | Post-processes the restored image/video tone against the source. `wavelet` = wavelet tone reconstruction (default); `lab` = LAB tone matching; `off` = raw model output without tone correction. Default: wavelet. | `wavelet`, `lab`, `off` |
| `--vae-tiling` | Forces tiled VAE encode/decode. By default, small outputs stay untiled and large outputs automatically use tiled decode. | Boolean flag |
| `--start-seconds` **START_SECONDS** | For video inputs, skip frames before this source timestamp in seconds. | Decimal number (e.g. `5.0`, `10.5`) |
| `--max-frames` **MAX_FRAMES** | For video inputs, decode at most this many frames after `--start-seconds`. | Integer (e.g. `100`, `500`) |
| `--drop-audio` | For video inputs with source audio, opt out of the default audio-preservation contract and publish a silent restored MP4 intentionally. | Boolean flag |
| `--temporal-chunk-size` **TEMPORAL_CHUNK_SIZE** | For video inputs, restore this many source frames per chunk before stitching. Prefer official `4n+1` sizes such as `45` or `49`. Default: 49. | Integer (e.g. `45`, `49`, `65`) |
| `--temporal-chunk-overlap` **TEMPORAL_CHUNK_OVERLAP** | For video inputs, reuse this many source frames as context between adjacent chunks. This is context overlap, not an output crossfade. Default: 16. | Integer (e.g. `16`, `8`) |
| `--force-unsafe-video-memory` | Bypasses SeedVR2 video memory safety checks. Use only when you are intentionally accepting the risk of machine instability or process failure. | Boolean flag |
| `--no-validate-health` | For video inputs, skip the post-save full-file health re-decode. For embedded hosts that probe the saved file themselves; the skip is recorded as `health_check=skipped`. | Boolean flag |

---

### 3. `mlxgen capabilities` Command

Inspects the public tasks, internal modes, and option support for a model.

| Argument | Description | Possible Values / Examples |
|----------|-------------|---------------------------|
| `--model`, `-m` **MODEL** | Model alias, Hugging Face repo, or local model path. | `flux2-klein-4b`, `qwen-image-edit-2509-8bit`, etc. |
| `--base-model` **BASE_MODEL** | Base model hint for custom repositories or local paths. | Any valid model alias |
| `--family` **{qwen, flux2, fibo, z-image, ernie-image, wan, bonsai}** | Overrides automatic family detection for the model. Use for local paths or custom repo names. | `qwen`, `flux2`, `fibo`, `z-image`, `ernie-image`, `wan`, `bonsai` |

---

### 4. `mlxgen validation` Command

Inspects release-validation evidence for exact model/package rows. This is separate from route capabilities and does not control `mlxgen generate`.

| Argument | Description | Possible Values / Examples |
|----------|-------------|---------------------------|
| `--model`, `-m` **MODEL** | Model alias, Hugging Face repo, or local model path. | Any valid model |
| `--profile` **PROFILE** | Validation profile ID. Defaults to the first profile with evidence for the requested model, or the current I2I edit 5x4 profile when no model-specific evidence exists. | Profile string (e.g. `"i2i-edit-5x4"`) |
| `--list` | Lists available validation profiles instead of returning profile/model rows. | Boolean flag |

---

### 5. `mlxgen download` Command

Explicitly downloads a Hugging Face model snapshot into the local cache.

| Argument | Description | Possible Values / Examples |
|----------|-------------|---------------------------|
| `--model`, `-m` **MODEL** | Model alias or Hugging Face repo ID. | `Qwen/Qwen-Image`, `abstractframework/model`, etc. |
| `--base-model` **BASE_MODEL** | Base model hint for custom repositories. | Any valid model alias |
| `--all-files` | Downloads the full repository instead of only the MLX-Gen weight/tokeniser patterns. | Boolean flag |

---

### 6. `mlxgen prepare` Command

Prepares a reusable local MLX-Gen model folder, optionally quantised, and writes a Hugging Face model card.

| Argument | Description | Possible Values / Examples |
|----------|-------------|---------------------------|
| `--model`, `-m` **MODEL** | The model to use (dev or schnell or krea-dev or schnell-krea/qwen/qwen-image/qwen-image-edit/qwen-image-edit-2509/qwen-image-edit-2511/qwen-edit/qwen-edit-plus/qwen-edit-2509/qwen-edit-2511/fibo/fibo-lite/fibo-edit/fibo-edit-rmbg/z-image/z-image-turbo/ernie-image-turbo/seedvr2/seedvr2-3b/seedvr2-7b/seedvr2-7b-sharp/wan2.2-ti2v-5b/bonsai-image-ternary/bonsai-image-binary/flux2-klein-4b/flux2-klein-9b/flux2-klein-base-4b/flux2-klein-base-9b, a HuggingFace repo org/model, or a local path). | **Qwen**: `qwen`, `qwen-image`, `qwen-image-edit`, `qwen-image-edit-2509`, `qwen-image-edit-2511`, `qwen-edit`, `qwen-edit-plus`, `qwen-edit-2509`, `qwen-edit-2511`<br>**FLUX.2**: `flux2-klein-4b`, `flux2-klein-9b`, `flux2-klein-base-4b`, `flux2-klein-base-9b`<br>**Z-Image**: `z-image`, `z-image-turbo`<br>**SeedVR2**: `seedvr2`, `seedvr2-3b`, `seedvr2-7b`, `seedvr2-7b-sharp`<br>**Wan**: `wan2.2-ti2v-5b`<br>**Fibo**: `fibo`, `fibo-lite`, `fibo-edit`, `fibo-edit-rmbg`<br>**Others**: `ernie-image-turbo`, `bonsai-image-ternary`, `bonsai-image-binary` |
| `--path` **PATH** | Local path for saving a model to disk. | Directory path: `./models/qwen-image-8bit` |
| `--base-model` **BASE_MODEL** | Base model alias or upstream repo ID for prepared/custom checkpoints. | Any valid model alias |
| `--quantize`, `-q` **{3, 5, 4, 6, 8}** | Quantises the model. Default: None. | `3`, `4`, `5`, `6`, `8` bits |
| `--lora-paths` **[LORA_PATHS ...]** | LoRA paths: local files, HuggingFace repos (org/model), or collection format (repo:filename.safetensors). | List of paths or repos: `org/model`, `repo:weights.safetensors` |
| `--lora-scales` **[LORA_SCALES ...]** | Scaling factor to adjust the impact of LoRA weights on the model. A value of `1.0` applies the LoRA weights as they are. | List of decimals: `1.0`, `0.8`, `1.2` |

#### LoRA Configuration (prepare)

| Argument | Description | Possible Values / Examples |
|----------|-------------|---------------------------|
| `--lora-style` **{couple, font, home, identity, illustration, portrait, ppt, sandstorm, sparklers, storyboard}** | Style of the LoRA to use (e.g. `'storyboard'` for film storyboard style). | `couple`, `font`, `home`, `identity`, `illustration`, `portrait`, `ppt`, `sandstorm`, `sparklers`, `storyboard` |

---

## Summary of Supported Model Families

| Family | Description | Main Models |
|--------|-------------|-------------|
| **qwen** | Qwen Image models for text-to-image and image editing | `qwen`, `qwen-image`, `qwen-image-edit`, `qwen-edit`, `qwen-edit-plus` |
| **flux2** | FLUX.2 models (Klein variants) | `flux2-klein-4b`, `flux2-klein-9b`, `flux2-klein-base-4b`, `flux2-klein-base-9b` |
| **fibo** | Fibo models for image generation/editing | `fibo`, `fibo-lite`, `fibo-edit`, `fibo-edit-rmbg` |
| **z-image** | Z-Image models for text-to-image | `z-image`, `z-image-turbo` |
| **ernie-image** | Ernie Image models | `ernie-image-turbo` |
| **wan** | Wan models for video generation | `wan2.2-ti2v-5b` |
| **bonsai** | Bonsai models (ternary/binary) | `bonsai-image-ternary`, `bonsai-image-binary` |

## Supported Tasks Evidence

| Task | Abbreviations | Description |
|------|--------------|-------------|
| **text-to-image** | `txt2img` | Generates an image from a text prompt |
| **image-to-image** | `img2img` | Modifies/Varies an existing image |
| **edit** | - | Edits an image with text instructions |
| **text-to-video** | `txt2vid`, `t2v` | Generates a video from a text prompt |
| **image-to-video** | `img2vid`, `i2v` | Generates a video from an image (first frame) |
| **video-to-video** | `vid2vid`, `v2v` | Modifies an existing video with a prompt |
