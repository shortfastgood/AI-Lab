#!/bin/bash
cd ~/gitroot/ComfyUI
source venv/bin/activate
export HF_HOME="$HOME/ComfyUI/.cache/huggingface"
export PYTORCH_ENABLE_MPS_FALLBACK=1
python main.py