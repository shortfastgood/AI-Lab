# May 2026 - Goodbye, GitHub Copilot?

GitHub Copilot was the forerunner of a whole generation of agents that turn a prompt into an answer, working code, or a concrete action. Since 2023, that list has become extremely long. I stayed loyal to Copilot as my first choice, even though I also use Claude and Codex in parallel. Copilot has been successful, and it is now, in some ways, a victim of that success.

Until now, paid plans were billed per request. From 1 June, they will be billed in Credits: an abstract unit that makes it much harder to understand quickly and accurately what things actually cost.

It is obvious that request-based billing is no longer sustainable. Even so, hiding API costs behind an abstract unit is a questionable move. AI API pricing is already volatile because it depends on the model and on how we use it. With every new model, we should expect higher costs, because that has happened with striking regularity. At the same time, we are forced to follow model churn because models are retired so quickly. The result is an environment that is unstable both operationally and economically. The same applies to almost every competing product.

This is a negative development. It is not just getting more expensive; it also deepens our dependence on the major AI providers. These centres consume enormous resources, and there have already been cases where entire communities faced shortages of energy or water because of them. It also increases the risk of large-scale disruption, much as we have already seen with cloud infrastructure. Even today, if ChatGPT stops responding, people panic.

I have decided not to follow that path. Instead, I am moving towards models that run locally. It requires suitable hardware: for example, a MacBook Pro M4 Max with at least 64 GB of memory, and ideally 128 GB. The easiest setup I have found is still based on VS Code with GitHub Copilot, while the missing piece is provided by Ollama, which connects the model to Copilot.

There is a wide range of models that could work well enough, but my goal is to achieve a workflow broadly comparable to what I have had with the large hosted models. I deliberately avoided choosing on the basis of benchmarks, which I do not rate highly. My reference point instead was the **one-prompt-apps** project:

https://github.com/shortfastgood/one-prompt-apps/tree/main

Its core aim is to evaluate, using a single prompt, what an AI model can actually produce. The real question is always the same: does the output become a usable application with a decent design?

To begin with, I chose a model Alibaba released eight months ago: **Qwen3-Coder:30b**. Its specifications are **19 GB**, a **256k** context window, **qwen3moe** architecture, **30.5B** parameters, and **Q4_K_M** quantisation. In practice, this model could have given me a stable production environment from October 2025 right up to today.

In testing, Qwen3-Coder generated the application and all of its components from the very first prompt. Its speed was surprising. Strictly speaking, it was the weakest performance among the large models I had tested, but the gap was very small.

The game design it produced was simple, clean, and absolutely competitive with what Claude Sonnet generated. The JavaScript code was a little less refined than Claude Sonnet's, but the differences were marginal.

Qwen3-Coder did show some limits when it came to program functionality. It took six separate prompts to reach a genuinely working version. On the positive side, once I pointed out one malfunction, the agent immediately corrected three other errors as well and ran a test to confirm that the fixes worked. On the negative side, the responses became progressively slower. Session degradation was significant. To restore execution speed, I had to reset Ollama, which could also mean closing and reopening VS Code.

Overall, though, this is a highly respectable result at zero cost, despite a few inconveniences. In terms of efficiency, the Tetris version produced with Claude Sonnet took me about 90 minutes, including checks and tests. The Qwen3-Coder version took about four hours, again including checks and tests. Had I built a similar Tetris application manually, using only a keyboard and a conventional IDE, I would have had to budget at least three days.

For me, this first experience highlights something important: it is possible to step outside the logic of the major providers, where every improvement made by my company can be absorbed by the provider and then redistributed, for a fee, to every other customer. If I step away from that model, my progress and my ideas remain my own. That gives me a real chance to differentiate myself from competitors.
