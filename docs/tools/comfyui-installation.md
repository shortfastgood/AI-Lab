# ComfyUI Installation

Local installation of ComfyUI with a dedicated workspace environment.

## macOS

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
