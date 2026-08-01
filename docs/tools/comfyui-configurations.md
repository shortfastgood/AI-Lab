# ComfyUI Configurations

- [General](#general)
- [A local LLM for prompt generation](#a-local-llm-for-prompt-generation)
- [FLUX MLX Accellerator](#flux-mlx-accellerator)

## General

To more easily add models to ComfyUI it is recommended to install the **huggingface_hub** package.

    user@macbook % export HF_HOME="$HOME/gitroot/ComfyUI/.cache/huggingface"
    user@macbook % pip install huggingface_hub

## A local LLM for prompt generation

"*The LLM runs inside ComfyUI as a node, in the same process. Nothing extra to start. A good pick is mlx-vlm-ComfyUI, which loads an MLX vision-language model in-process — meaning it can expand a text idea into a prompt and, as a bonus, caption an input image for img2img-style prompting.*"

    user@macbook % cd ~/ComfyUI/custom_nodes
    user@macbook % git clone https://github.com/rurounigit/mlx-vlm-ComfyUI.git
    user@macbook % cd mlx-vlm-ComfyUI
    user@macbook % pip install -r requirements.txt

The Python module **mlx_vlm** was added to the environment reducing node warnings while running ComfyUI.

## FLUX MLX Accellerator

"*The ComfyUI-MLX nodes reimplement Flux using Apple's MLX framework and Metal directly, and report meaningful speedups on Apple Silicon (their figures: ~70% faster when the model has to load, ~35% faster when it's already resident, and ~30% lower memory use).*"

    user@macbook % cd ~/ComfyUI/custom_nodes
    user@macbook % git clone https://github.com/raysers/ComfyUI-MLX.git
    user@macbook % cd ComfyUI-MLX
    user@macbook % pip install -r requirements.txt

The Python module **argmaxtools** was added to the environment reducing node warnings while running ComfyUI.


