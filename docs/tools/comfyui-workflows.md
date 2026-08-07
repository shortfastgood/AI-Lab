# ComfyUI Workflows

## SDXL Simple image Generation

     % cd ~/gitroot/ComfyUI

## Required Models

Caffeinate prevents the download from being interrupted if the user leaves their workstation for an extended period. Downloads the base model.

     % caffeinate -i hf download stabilityai/stable-diffusion-xl-base-1.0/sd_xl_base_1.0.safetensors --local-dir ./models/checkpoints/

Download the refinement model.

     % caffeinate -i hf download stabilityai/stable-diffusion-xl-refiner-1.0\sd_xl_refiner_1.0.safetensors --local-dir ./models/checkpoints/

## Flow

- Start or restart ComfyUI 
- Connect to http://127.0.0.1:8188 with the WEB browser.
- Select the Templates icon.
- Select generation type image.
- Search for SDXL
- Select the SDXL Simple template
- Press the run button.

<img src="../../docs/images/ComfyUI_SDXL_simple.png" width=720>
