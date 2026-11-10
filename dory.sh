#!/bin/bash
cd ~/gitroot/llama.cpp-dory
./build/bin/llama-server \
    -m ./dory/NVIDIA-Nemotron-Labs-Dory1.0-4B-Q5_K_M.gguf\
    --alias dory \
    --host 127.0.0.1 --port 8080 \
    -ngl 999 \
    --ctx-size 4096 --parallel 1 \
    --batch-size 512 --ubatch-size 512 \
    --cache-type-k f16 --cache-type-v f16 \
    --flash-attn off \
    --no-context-shift \
    --jinja --reasoning on \
    --temp 1.0 --top-p 0.95 --top-k 0 --min-p 0 --repeat-penalty 1 \
    --override-kv "dory.num_loops=int:2,dory.recurrent_kv_cache_mode=str:per_loop"
