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

Per aggiungere più facilmente modelli a ComfyUI è consigliabile aggiungere il pacchetto **huggingface_hub**.

    user@macbook % export HF_HOME="$HOME/ComfyUI/.cache/huggingface"
    user@macbook % pip install huggingface_hub

### SDLX

Caffeinate impedisce l'interruzione del download nel caso l'utente lasci la postazione di lavoro per lungo tempo

     user@macbook % caffeinate -i\
      hf download stabilityai/stable-diffusion-xl-base-1.0\
      sd_xl_base_1.0.safetensors\
      --local-dir ./models/checkpoints/
