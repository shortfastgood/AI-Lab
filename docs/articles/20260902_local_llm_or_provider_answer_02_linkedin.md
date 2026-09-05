I'm weighing two approaches: the classic chat-based one (see https://github.com/shortfastgood/one-prompt-apps) and a tool purpose-built for the job.

For image processing I started with ComfyUI (https://github.com/comfy-org/comfyui) — see https://github.com/shortfastgood/AI-Lab/blob/master/docs/tools/comfyui.md. It's excellent, but generally slow on macOS: it was built for a PC plus an NVIDIA card. To get the best results, including performance, on macOS you need Apple's MLX framework.

I went with MLXGen (https://github.com/shortfastgood/AI-Lab/blob/master/docs/tools/mlxgen.md), but that alone is not enough: you also need a right-sized, specialised model such as Black Forest Labs' FLUX.2-klein-4B.

The results are strong when the prompts are simple and precise and the source images are suitable, for example, for a blog. Large, high-resolution photographic images still take time and a lot of memory.
