# ComfyUI

## Installation

Installed locally with a dedicated workspace environment.

    user@macbook % cd gitroot\
                   & git clone https://github.com/comfyanonymous/ComfyUI.git\
                   & cd ComfyUI

Dedicated Python workspace environment.

    user@macbook % python3.14 -m venv venv
    user@macbook % source venv/bin/activate

Install ComfyUI on the Metal (MPS) backend.

    user@macbook % pip install --upgrade pip
    user@macbook % pip install torch torchvision torchaudio

Now install ComfyUI’s own dependencies.

    user@macbook % pip install -r requirements.txt

Check if MPS is available.

    user@macbook % python -c "import torch; print('MPS available:',\
                               torch.backends.mps.is_available())"

## Configuration

To more easily add models to ComfyUI it is recommended to install the **huggingface_hub** package.

    user@macbook % export HF_HOME="$HOME/gitroot/ComfyUI/.cache/huggingface"
    user@macbook % pip install huggingface_hub

### A local LLM for prompt generation

"*The LLM runs inside ComfyUI as a node, in the same process. Nothing extra to start. A good pick is mlx-vlm-ComfyUI, which loads an MLX vision-language model in-process — meaning it can expand a text idea into a prompt and, as a bonus, caption an input image for img2img-style prompting.*"

    user@macbook % cd ~/ComfyUI/custom_nodes
    user@macbook % git clone https://github.com/rurounigit/mlx-vlm-ComfyUI.git
    user@macbook % cd mlx-vlm-ComfyUI
    user@macbook % pip install -r requirements.txt

The Python module **mlx_vlm** is added to the environment to suppres a node warning.

### FLUX

#### MLX Accellerator

"*The ComfyUI-MLX nodes reimplement Flux using Apple's MLX framework and Metal directly, and report meaningful speedups on Apple Silicon (their figures: ~70% faster when the model has to load, ~35% faster when it's already resident, and ~30% lower memory use).*"

    user@macbook % cd ~/ComfyUI/custom_nodes
    user@macbook % git clone https://github.com/raysers/ComfyUI-MLX.git
    user@macbook % cd ComfyUI-MLX
    user@macbook % pip install -r requirements.txt

#### Models

The Python module **argmaxtools** is added to the environment to suppres a node warning.


### Multiple Angles



### SDXL

Simple image generation.

#### Models

Caffeinate prevents the download from being interrupted if the user leaves their workstation for an extended period. Downloads the base model.

     user@macbook % caffeinate -i\
      hf download stabilityai/stable-diffusion-xl-base-1.0\
      sd_xl_base_1.0.safetensors\
      --local-dir ./models/checkpoints/

Download the refinement model.

     user@macbook % caffeinate -i\
      hf download stabilityai/stable-diffusion-xl-refiner-1.0\
      sd_xl_refiner_1.0.safetensors\
      --local-dir ./models/checkpoints/

#### Test

- Start or restart ComfyUI 
- Connect to http://127.0.0.1:8188 with the WEB browser.
- Select the Templates icon.
- Select generation type image.
- Search for SDXL
- Select the SDXL Simple template
- Press the run button.

<img src="../../test/data/image/ComfyUI_SDXL_simple.png" width=720>


