# ComfyUI

| component | version |
|-----------|---------|
| ComfyUI   | 0.29.0  |
| frontend  | 1.47.10 |
| templates | 0.11.19 |
 
 ## Table of Contents
- [Installation](comfyui-installation.md)
- [Configurations](comfyui-configurations.md)
  - [General](comfyui-configurations.md#general)
  - [A local LLM for prompt generation](comfyui-configurations.md#a-local-llm-for-prompt-generation)
  - [FLUX MLX Accellerator](comfyui-configurations.md#flux-mlx-accellerator)
- [Workflows](comfyui-workflows.md)
  - [SDXL Simple Image Generation](comfyui-workflows.md#sdxl-simple-image-generation)

## Multiple Angles Workflow

This workflow is described by [SOTAI on YouTube](https://www.youtube.com/watch?v=4pm1Fp8lt6I); follow their instructions to obtain the complete workflow.

### Custom Nodes

#### ComfyUI-qwenmultiangle

"*A ComfyUI custom node for 3D camera angle control. Provides an interactive Three.js viewport to adjust camera angles and outputs formatted prompt strings for multi-angle image generation.*"

    user@macbook % cd ~/gitroot/ComfyUI/custom_nodes
    user@macbook % git clone https://github.com/jtydhr88/ComfyUI-qwenmultiangle

#### KJNodes for ComfyUI

"*At this point pretty random collection of utility, model optimization and QoL nodes, while keeping dependencies at minimum.*"

    user@macbook % cd ~/gitroot/ComfyUI/custom_nodes
    user@macbook % git clone https://github.com/kijai/ComfyUI-KJNodes
    user@macbook % cd ComfyUI-KJNodes
    user@macbook % pip install -r requirements.txt

### Required Models

    user@macbook % cd ~/gitroot/ComfyUI

#### UNET

    user@macbook % caffeinate -i\
                   hf download hf://Comfy-Org/Qwen-Image-Edit_ComfyUI/split_files/diffusion_models/qwen_image_edit_2511_bf16.safetensors\
                     --localdir ./models/unet

#### LORA

    user@macbook % caffeinate -i\
                   hf download hf://lightx2v/Qwen-Image-Edit-2511-Lightning/Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors\
                     --localdir ./models/loras

    user@macbook % caffeinate -i\
                   hf download hf://fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA/qwen-image-edit-2511-multiple-angles-lora.safetensors\
                     --localdir ./models/loras

#### VAE

    user@macbook % caffeinate -i\
                   hf download hf://Comfy-Org/Qwen-Image_ComfyUI/split_files/vae/qwen_image_vae.safetensors\
                     --localdir ./models/vae

#### TEXT ENCODERS

    user@macbook % caffeinate -i\
                   hf download hf://Comfy-Org/Qwen-Image_ComfyUI/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors\
                     --localdir ./models/text_encoders

## References

- [ComfyUI + MLX on Apple Silicon: The Clean, Native Setup](https://medium.com/@michael.hannecke/comfyui-mlx-on-apple-silicon-the-clean-native-setup-9dfaa9932a4d)
- [Consistent Multishots Made Easy: Qwen Image Edit Multi Angles LoRA (ComfyUI Workflow)](https://www.patreon.com/SOTAI/posts/consistent-made-148036093?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link)