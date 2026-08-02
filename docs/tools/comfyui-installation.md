# ComfyUI Installation

Local installation of ComfyUI with a dedicated workspace environment.

## macOS

    % cd gitroot
    % git clone https://github.com/comfyanonymous/ComfyUI.git\
    % cd ComfyUI

Dedicated Python workspace environment.

    % python3.14 -m venv venv
    % source venv/bin/activate

Install ComfyUI on the Metal (MPS) backend.

    % pip install --upgrade pip
    % pip install torch torchvision torchaudio

Now install ComfyUI’s own dependencies.

    % pip install -r requirements.txt

Check if MPS is available.

    % python -c "import torch; print('MPS available:', torch.backends.mps.is_available())"
