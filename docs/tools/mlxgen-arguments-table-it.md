# Tabella degli Argomenti di MLX-Gen (MLX Framework - Apple)

**Programma:** `mlxgen` (MLX-Gen CLI)  
**Versione:** 0.25.0 (2026-07-25)  
**Sottocomandi principali:** `generate`, `upscale`, `capabilities`, `validation`, `download`, `prepare`

---

## Tabella degli Argomenti per Sottocomando

### 1. Comando `mlxgen generate`

Genera immagini o video, e modifica immagini, da un modello preparato o in cache.

| Argomento | Descrizione | Possibili Valori / Esempi |
|-----------|-------------|--------------------------|
| `--model`, `-m` **MODEL** | Model alias, Hugging Face repo, o percorso locale del modello. | `z-image-turbo`, `wan2.2-ti2v-5b`, `flux2-klein-4b`, oppure un percorso locale come `./models/qwen-image` |
| `--base-model` **BASE_MODEL** | Base model hint per repository custom o percorsi locali. | Qualsiasi model alias valido |
| `--family` **{qwen, flux2, fibo, z-image, ernie-image, wan, bonsai}** | Override della detection automatica della famiglia del modello. Utilizzare per percorsi locali o nomi di repo custom. | `qwen`, `flux2`, `fibo`, `z-image`, `ernie-image`, `wan`, `bonsai` |
| `--debug` | Abilita logging debug per dettagli interni della generazione (es. LoRA fusion targets). | Flag booleano, nessun valore richiesto |
| `--task` **{auto, text-to-image, txt2img, image-to-image, img2img, edit, text-to-video, txt2vid, t2v, image-to-video, img2vid, i2v, video-to-video, vid2vid, v2v}** | Override del routing automatico. Default: auto. | `auto`, `text-to-image` (`txt2img`), `image-to-image` (`img2img`), `edit`, `text-to-video` (`txt2vid`, `t2v`), `image-to-video` (`img2vid`, `i2v`), `video-to-video` (`vid2vid`, `v2v`) |
| `--i2i-mode` **{auto, latent, img2img, edit, edit-reference, multi, multi-reference}** | Modalità interna image-to-image. Default: auto. Usa `latent/img2img` per variazioni di image-strength, `edit` per modifiche basate su istruzioni/riferimento, o `multi-reference` per due o più immagini di input. | `auto`, `latent`, `img2img`, `edit`, `edit-reference`, `multi`, `multi-reference` |
| `--image`, `--input-image`, `-i` **IMAGES** | Immagine di input. Usa una immagine per image-to-image o Wan first-frame image-to-video. Ripeti solo per multi-reference image-to-image. | Percorso a file immagine: `.png`, `.jpg`, ecc. |
| `--images`, `--input-images`, `--image-paths` **IMAGE_GROUPS [...]** | Una o più immagini di input per modalità image-to-image reference/edit. | Lista di percorsi a file immagine |
| `--image-path` **IMAGE_PATH** | Alias di compatibilità per singola immagine di input, incluso Wan first-frame image-to-video. | Percorso a file immagine |
| `--video`, `--input-video` **VIDEOS** | Video sorgente per route plain prompt-guided video-to-video. | Percorso a file video: `.mp4`, ecc. |
| `--video-path` **VIDEO_PATH** | Alias di compatibilità per singolo video sorgente su plain video-to-video routes. | Percorso a file video |
| `--video-strength` **VIDEO_STRENGTH** | Denoising strength per plain video-to-video routes. Valori più alti permettono cambiamenti d'aspetto maggiori. | Numero decimale (es. `0.5`, `0.8`) |
| `--video-mask-path` **VIDEO_MASK_PATH** | Maschera immagine statica per masked video-to-video. Il bianco indica la regione che il modello può cambiare; il nero viene preservato esattamente dal video sorgente. | Percorso a file maschera immagine (PNG) |
| `--reframe-padding` **REFRAMES_PADDING** | Richiesta di generative reframe: padding CSS-style `top,right,bottom,left`. Modelli edit supportano ridisegno su canvas più grande. Non è masked outpainting e non preserva i pixel sorgente esattamente. | CSS-style: `0,25%,0,25%`, `10px,10px,10px,10px` |
| `--outpaint-padding`, `--image-outpaint-padding` **OUTPAINT_PADDING** | Richiesta canvas outpaint: padding CSS-style `top,right,bottom,left`. Qwen Image Edit usa generative canvas expansion con adaptive source restoration. FLUX.2 richiede base Klein model e usa source-locked denoising. | CSS-style: `0,25%,0,25%`, `50px,50px,50px,50px` |

#### Opzioni Comuni di Generazione (forwarded al backend selezionato)

| Argomento | Descrizione | Possibili Valori / Esempi |
|-----------|-------------|--------------------------|
| `--prompt` | Prompt testuale per descrivere l'immagine/video da generare. | Stringa libera: `"A puffin standing on a cliff"` |
| `--prompt-file` | Legge il prompt da un file. | Percorso a file `.txt` |
| `--width` | Larghezza in pixel dell'output. | Numero intero (es. `1024`, `1280`) |
| `--height` | Altezza in pixel dell'output. | Numero intero (es. `768`, `1024`) |
| `--steps` | Numero di passi di diffusione. | Numero intero (es. `30`, `50`) |
| `--guidance` | Guidance scale per il controllo del prompt. | Numero decimale (es. `7.5`, `9.0`) |
| `--seed` | Seed di entropia per riproducibilità. | Numero intero positivo (es. `42`) |
| `--auto-seeds` | Auto-genera N entropy seeds (random ints tra 0 e 10,000,000). | Numero intero (es. `5` = genera 5 seed random) |
| `--negative-prompt`, `--negative` | Prompt negativo per escludere elementi dall'output. | Stringa libera: `"blurry, low quality"` |
| `--canvas-policy` | Policy di gestione del canvas. | Valore specifico del backend |
| `--resize-mode` | Modalità di ridimensionamento (latent image-to-image e Wan video routes). | Valore specifico del backend |
| `--quantize` | Quantizzazione del modello. | `3`, `4`, `5`, `6`, `8` bit |
| `--lora-paths` | Percorsi LoRA: file locali, HuggingFace repos (org/model), o formato collection (repo:filename.safetensors). | Lista di percorsi o repo ID |
| `--lora-scales` | Fattore di scaling per l'impatto dei pesi LoRA sul modello. `1.0` applica i pesi così come sono. | Lista di numeri decimali (es. `1.0`, `0.8`) |
| `--mask-path` | Percorso a maschera per edit localizzato o inpaint su modelli che supportano masked edit/inpaint. | Percorso a file immagine PNG |
| `--controlnet-image-path` | Percorso a immagine ControlNet per controllo strutturato su route text-to-image. Differenti da source-image editing. | Percorso a file immagine |
| `--controlnet-strength` | Strength del ControlNet. | Numero decimale (es. `0.8`) |
| `--metadata` | Esporta metadata immagine come file JSON. | Flag booleano |
| `--embed-metadata` | Embed metadata nell'immagine salvata. Default: off. | Flag booleano |
| `-C`, `--config-from-metadata` | Configura da metadata preesistenti. | Flag booleano |
| `--output` | Filename per l'output immagine/video. Supporta `{seed}` e `{input_name}` quando si elaborano più sorgenti. Default: `"image.png"`. | Stringa: `"result.png"`, `"video_{seed}.mp4"` |
| `--replace` | Sostituisce file output esistente se esiste. | Flag booleano |
| `--frames` | Numero di frame per video. | Numero intero |
| `--fps` | Frame per second per video. | Numero intero (es. `24`, `30`) |
| `--guidance-2` | Seconda guidance scale. | Numero decimale |
| `--flow-shift` | Flow shift parameter. | Numero decimale |
| `--low-ram` | Abilita low-RAM mode per ridurre uso memoria (può impattare performance). | Flag booleano |
| `--tensor-health-check-interval` | Intervallo per health check tensori. | Numero intero (ms) |
| `--json-events` | Emette eventi JSONL machine-readable a stdout, testo CLI su stderr. | Flag booleano |
| `--keep-text-encoder` | Mantieni text encoder in memoria. | Flag booleano |
| `--no-prompt-cache` | Disabilita cache prompt. | Flag booleano |
| `--compile-transformer` | Compila transformer per performance. | Flag booleano |
| `--release-inactive-denoiser`, `--no-release-inactive-denoiser` | Release inactive denoiser (Wan routes). | Flag booleano |
| `--progress`, `--no-progress` | Mostra/disabilita CLI progress. Default: true. | Flag booleano |

---

### 2. Comando `mlxgen upscale`

Ripristina o upscalas immagini e video con SeedVR2 diffusion-based super-resolution.

| Argomento | Descrizione | Possibili Valori / Esempi |
|-----------|-------------|--------------------------|
| `--battery-percentage-stop-limit`, `-B` **BATTERY_PERCENTAGE_STOP_LIMIT** | Su Mac alimentati a batteria, ferma generazione quando la batteria arriva a questa percentuale. Default: 5 | Numero intero (es. `5`, `10`) |
| `--low-ram` | Abilita low-RAM mode per ridurre uso memoria. | Flag booleano |
| `--mlx-cache-limit-gb` **MLX_CACHE_LIMIT_GB** | Limita cache MLX in GB senza abilitare full low-RAM mode. Default: machine-derived (total RAM / 8, clamped 1-8 GiB). `-1` = unlimited. | Numero intero o `-1`: `8`, `16`, `-1` |
| `--debug` | Abilita logging debug per dettagli interni. | Flag booleano |
| `--json-events` | Emette eventi JSONL machine-readable a stdout. | Flag booleano |
| `--progress`, `--no-progress` | Mostra/disabilita CLI progress. Default: true. | Flag booleano |
| `--model`, `-m` **MODEL** | SeedVR2 model alias, official HF repo, AbstractFramework SeedVR2 package, o percorso locale. | `seedvr2`, `seedvr2-3b`, `seedvr2-7b`, `seedvr2-7b-sharp` |
| `--base-model` **BASE_MODEL** | Base model alias o upstream repo id per prepared/custom checkpoints. | Qualsiasi model alias valido |
| `--quantize`, `-q` **{3, 5, 4, 6, 8}** | Quantizza il modello. Default: None. | `3`, `4`, `5`, `6`, `8` bit |
| `--metadata` | Esporta metadata immagine come file JSON. | Flag booleano |
| `--embed-metadata` | Embed metadata nell'immagine salvata. Default: off. | Flag booleano |
| `--output` **OUTPUT** | Filename per output immagine/video. Supporta `{seed}` e `{input_name}`. Default: `"image.png"`. | Stringa: `"upscaled.png"` |
| `--replace [REPLACE]` | Sostituisce file output esistente se esiste. `--replace false` o `--no-replace` preserva file esistente con percorso suffisso. | Flag con valore opzionale: `true`, `false` |
| `--no-replace` | Non sostituire file esistente; salva con nome suffissato. | Flag booleano |
| `--stepwise-image-output-dir` **[ESPERIMENTAL]** | Directory output per immagini step-wise e composite image finale. Feature può cambiare in versioni future. | Percorso directory |

#### Configurazione SeedVR2 Upscale

| Argomento | Descrizione | Possibili Valori / Esempi |
|-----------|-------------|--------------------------|
| `--image-path`, `-i` **IMAGE_PATH [...]** | Percorso immagine(i) o directory da upscalas. | Lista di percorsi `.png`, `.jpg` o directory |
| `--video-path` **VIDEO_PATH [...]** | Percorso video(i) o directory da ripristinare/upscales. | Lista di percorsi `.mp4` o directory |
| `--seed`, `-s` **SEED [...]** | Specifica 1+ Entropy Seeds. Default: 1 time-based random seed. | Lista di numeri interi: `42`, `123`, `456` |
| `--auto-seeds` **AUTO_SEEDS** | Auto-genera N entropy seeds (random ints tra 0 e 10,000,000). | Numero intero (es. `5` = genera 5 seed) |
| `--resolution`, `-r` **RESOLUTION** | Risoluzione target per shortest edge (pixels) o scale factor. Per video, omitting `--resolution` default a `1x`. | Scala: `2x`, `3x`; oppure pixel: `1024`, `2048` |
| `--softness` **SOFTNESS** | Valore tra 0.0 (off, factor 1) e 1.0 (max, factor 8). Default: 0.0. | Decimale: `0.0`, `0.5`, `1.0` |
| `--color-correction` **{wavelet, lab, off}** | Post-processa tono immagine/video contro sorgente. `wavelet` = wavelet tone reconstruction (default); `lab` = LAB tone matching; `off` = raw output senza correction. | `wavelet`, `lab`, `off` |
| `--vae-tiling` | Forza tiled VAE encode/decode. Default: piccolo output untiled, grande automaticamente tiled. | Flag booleano |
| `--start-seconds` **START_SECONDS** | Per video input, salta frames prima di questo timestamp in secondi. | Numero decimale (es. `5.0`, `10.5`) |
| `--max-frames` **MAX_FRAMES** | Per video input, decodera al massimo questo numero di frames dopo `--start-seconds`. | Numero intero (es. `100`, `500`) |
| `--drop-audio` | Per video con audio sorgente, skip preservation audio e pubblica MP4 silenzioso intenzionalmente. | Flag booleano |
| `--temporal-chunk-size` **TEMPORAL_CHUNK_SIZE** | Per video input, ripristina questo numero di source frames per chunk prima di stitch. Preferisci formati `4n+1` come `45` o `49`. Default: 49. | Numero intero (es. `45`, `49`, `65`) |
| `--temporal-chunk-overlap` **TEMPORAL_CHUNK_OVERLAP** | Per video input, riutilizza questo numero di source frames come context tra chunk adiacenti. Context overlap, non output crossfade. Default: 16. | Numero intero (es. `16`, `8`) |
| `--force-unsafe-video-memory` | Bypass SeedVR2 video memory safety checks. Usa solo accettando rischio instabilità/macchina o failure processo. | Flag booleano |
| `--no-validate-health` | Per video input, skip full-file health re-decode post-save. Hosted probe self possono fare skip; registrato come `health_check=skipped`. | Flag booleano |

---

### 3. Comando `mlxgen capabilities`

Ispeziona public tasks, internal modes, e option support per un modello.

| Argomento | Descrizione | Possibili Valori / Esempi |
|-----------|-------------|--------------------------|
| `--model`, `-m` **MODEL** | Model alias, Hugging Face repo, o percorso locale del modello. | `flux2-klein-4b`, `qwen-image-edit-2509-8bit`, ecc. |
| `--base-model` **BASE_MODEL** | Base model hint per custom repositories o percorsi locali. | Qualsiasi model alias valido |
| `--family` **{qwen, flux2, fibo, z-image, ernie-image, wan, bonsai}** | Override della detection automatica famiglia modello. Utilizzare per percorsi locali o nomi di repo custom. | `qwen`, `flux2`, `fibo`, `z-image`, `ernie-image`, `wan`, `bonsai` |

---

### 4. Comando `mlxgen validation`

Ispeziona release-validation evidence per esatti model/package rows. Separato dalle route capabilities e non controlla `mlxgen generate`.

| Argomento | Descrizione | Possibili Valori / Esempi |
|-----------|-------------|--------------------------|
| `--model`, `-m` **MODEL** | Model alias, Hugging Face repo, o percorso locale del modello. | Qualsiasi model valido |
| `--profile` **PROFILE** | Validation profile ID. Default: first profile con evidence per modello richiesto, oppure current I2I edit 5x4 profile quando nessuna evidence specifica esiste. | Stringa profilo (es. `"i2i-edit-5x4"`) |
| `--list` | Lista available validation profiles invece di restituire rows profilo/model. | Flag booleano |

---

### 5. Comando `mlxgen download`

Download esplicitamente un Hugging Face model snapshot nella locale cache.

| Argomento | Descrizione | Possibili Valori / Esempi |
|-----------|-------------|--------------------------|
| `--model`, `-m` **MODEL** | Model alias o Hugging Face repo ID. | `Qwen/Qwen-Image`, `abstractframework/model`, ecc. |
| `--base-model` **BASE_MODEL** | Base model hint per custom repositories. | Qualsiasi model alias valido |
| `--all-files` | Download full repository invece di solo MLX-Gen weight/tokenizer patterns. | Flag booleano |

---

### 6. Comando `mlxgen prepare`

Prepara una reusable local MLX-Gen model folder, opzionalmente quantizzata, e scrive Hugging Face model card.

| Argomento | Descrizione | Possibili Valori / Esempi |
|-----------|-------------|--------------------------|
| `--model`, `-m` **MODEL** | Il modello da usare. Dev/schnell/krea-dev/schnell-krea/qwen/qwen-image/qwen-image-edit/qwen-image-edit-2509/qwen-image-edit-2511/qwen-edit/qwen-edit-plus/qwen-edit-2509/qwen-edit-2511/fibo/fibo-lite/fibo-edit/fibo-edit-rmbg/z-image/z-image-turbo/ernie-image-turbo/seedvr2/seedvr2-3b/seedvr2-7b/seedvr2-7b-sharp/wan2.2-ti2v-5b/bonsai-image-ternary/bonsai-image-binary/flux2-klein-4b/flux2-klein-9b/flux2-klein-base-4b/flux2-klein-base-9b, oppure HF repo org/model, o percorso locale. | **Qwen**: `qwen`, `qwen-image`, `qwen-image-edit`, `qwen-image-edit-2509`, `qwen-image-edit-2511`, `qwen-edit`, `qwen-edit-plus`, `qwen-edit-2509`, `qwen-edit-2511`<br>**FLUX.2**: `flux2-klein-4b`, `flux2-klein-9b`, `flux2-klein-base-4b`, `flux2-klein-base-9b`<br>**Z-Image**: `z-image`, `z-image-turbo`<br>**SeedVR2**: `seedvr2`, `seedvr2-3b`, `seedvr2-7b`, `seedvr2-7b-sharp`<br>**Wan**: `wan2.2-ti2v-5b`<br>**Fibo**: `fibo`, `fibo-lite`, `fibo-edit`, `fibo-edit-rmbg`<br>**Altri**: `ernie-image-turbo`, `bonsai-image-ternary`, `bonsai-image-binary` |
| `--path` **PATH** | Percorso locale per salvare modello su disco. | Percorso directory: `./models/qwen-image-8bit` |
| `--base-model` **BASE_MODEL** | Base model alias o upstream repo id per prepared/custom checkpoints. | Qualsiasi model alias valido |
| `--quantize`, `-q` **{3, 5, 4, 6, 8}** | Quantizza il modello. Default: None. | `3`, `4`, `5`, `6`, `8` bit |
| `--lora-paths` **[LORA_PATHS ...]** | LoRA paths: file locali, HuggingFace repos (org/model), o collection format (repo:filename.safetensors). | Lista di percorsi o repo: `org/model`, `repo:weights.safetensors` |
| `--lora-scales` **[LORA_SCALES ...]** | Fattore scaling per impatto LoRA weights sul modello. `1.0` applica pesi così come sono. | Lista decimali: `1.0`, `0.8`, `1.2` |

#### LoRA Configuration (prepare)

| Argomento | Descrizione | Possibili Valori / Esempi |
|-----------|-------------|--------------------------|
| `--lora-style` **{couple, font, home, identity, illustration, portrait, ppt, sandstorm, sparklers, storyboard}** | Style del LoRA da usare. Es: `'storyboard'` per film storyboard style. | `couple`, `font`, `home`, `identity`, `illustration`, `portrait`, `ppt`, `sandstorm`, `sparklers`, `storyboard` |

---

## Riepilogo delle Famiglie di Modelli Supportate

| Famiglia | Descrizione | Modelli Principali |
|----------|-------------|-------------------|
| **qwen** | Qwen Image models per text-to-image e image editing | `qwen`, `qwen-image`, `qwen-image-edit`, `qwen-edit`, `qwen-edit-plus` |
| **flux2** | FLUX.2 models (Klein variants) | `flux2-klein-4b`, `flux2-klein-9b`, `flux2-klein-base-4b`, `flux2-klein-base-9b` |
| **fibo** | Fibo models per image generation/editing | `fibo`, `fibo-lite`, `fibo-edit`, `fibo-edit-rmbg` |
| **z-image** | Z-Image models per text-to-image | `z-image`, `z-image-turbo` |
| **ernie-image** | Ernie Image models | `ernie-image-turbo` |
| **wan** | Wan models per video generation | `wan2.2-ti2v-5b` |
| **bonsai** | Bonsai models (ternary/binary) | `bonsai-image-ternary`, `bonsai-image-binary` |

## Evidenza delle Task Supportate

| Task | Abbreviazioni | Descrizione |
|------|--------------|-------------|
| **text-to-image** | `txt2img` | Genera immagine da prompt testuale |
| **image-to-image** | `img2img` | Modifica/Varia immagine esistente |
| **edit** | - | Edita immagine con istruzioni testuali |
| **text-to-video** | `txt2vid`, `t2v` | Genera video da prompt testuale |
| **image-to-video** | `img2vid`, `i2v` | Genera video da immagine (first frame) |
| **video-to-video** | `vid2vid`, `v2v` | Modifica video esistente con prompt |
