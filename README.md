# AI-Lab

## Table of Contents

- [Introduction](#introduction)
- [Technology Adoption Risks](#technology-adoption-risks)
- [Chat](#chat)
  - [ChatGPT](#chatgpt)
  - [Gemini](#gemini)
  - [Claude](#claude)
  - [Deepseek](#deepseek)
- [Digital Assistant](#digital-assistant)
  - [GitHub Copilot](#github-copilot)
  - [Vibe Coding Tools](#vibe-coding-tools)
  - [Prompt Engineering](#prompt-engineering)
    - [Prompt Engineering Subsection](prompts/prompts.md)
      - [ART with ChatGPT](prompts/ART/art_with_chat_gpt.md)
      - [Image functions](prompts/image/image_functions.md)
      - [Translator Functions](prompts/translator/translator_functions.md)
  - [Embedding LLMs into Applications](./llm-lab/readme.md)

## Introduction

This project aims to analyze the advantages and side effects of digital assisted work.

Initially, it is a collection of experiences using GitHub's Copilot and OpenAI's ChatGPT.



Then, in September 2023, the exploratory phase began for local LLM usage in applications that could not rely on cloud data storage. 
Until early 2025, my research had not been very successful, as it inevitably ended in resource-intensive tests with various models 
capable of operating on limited resources.

With the release of the deepseek-r1 model, things began to change. The 14b and 32b variants ran well on a standard notebook, 
though patience was still required to be compared to online models. Nonetheless, it was now possible to begin working with them.

## Technology Adoption Risks

The technology associated with LLM will not disappear, and thus ignoring it means still running the risk of being excluded 
from those emerging sectors and being penalized by those that will inevitably become obsolete.

In 2025, those who do not adopt AI face the greatest risks. In various software development sectors, AI is rapidly advancing, 
drastically reducing reliance on keyboards or mice and shifting developers toward more creative endeavours.

The significant risk for businesses is the potential emergence of a startup offering the same project in a shorter timeframe 
and at lower costs, all without compromising quality.

To counter this threat, organizations must plan to encourage developers to leave the secure environment of traditional IDEs 
in favor of programming tools that rely on natural language. This approach presents a genuine challenge for those unaccustomed 
to "speaking" directly to their computer.

Adoption also entails concrete risks, well characterized by a [specific section of OWASP](https://owasp.org/www-project-top-10-for-large-language-model-applications/).

However, the risks highlighted by OWASP are increasingly mitigated by the option to deploy models locally in a protected and 
secure environment.

## Chat
The Chat section is dedicated to the use of LLMs in the form of chatbots.

For various reasons, I use ChatGPT, even though I have no direct affiliation with OpenAI. Consequently, 
my knowledge of other solutions is sometimes limited and occasionally indirect (drawn from available literature).

### ChatGPT
[ChatGPT](https://chat.openai.com) was the first online service that enabled interaction with a large language model. 
It underwent significant development and remains a leading choice among moderately priced offerings ($20/month).

### Gemini
[Gemini](https://gemini.google.com) replaced Google's early attempts with Bard. The current service is competitive with ChatGPT, 
including in terms of cost (approximately $22/month).

### Claude
[Claude](https://claude.ai) is a product of Anthropic, a company founded by former OpenAI employees. 
Competitive with both ChatGPT and Gemini, the price is 20$/month.

### Deepseek
[Deepseek](https://chat.deepseek.com) proposes a new kind of model with advanced features that surpass competing solutions. 
At present, the chat requires no subscription and can be used entirely free of charge.

## Digital Assistant

The digital assistant is an interactive agent that assists users in carrying out actions or creating solutions in the digital realm.

I started with GitHub Copilot, which I have not completely abandoned yet, but it is time to move forward. One option would 
have been to replace IntelliJ/Visual Studio Code + Copilot with [Cursor](https://www.cursor.com) or [Windsurf](ttps://codeium.com/windsurf). 
Both of these editors offer the ability to program with suggestions, as before, or to delegate code management to the agent 
and program using natural language commands.

~~I have opted for a more radical approach and decided to adopt the "[vibe coding](https://en.wikipedia.org/wiki/Vibe_coding)" technique, 
with as few compromises as possible.~~

**Update May 2025**.

Vibe coding did not meet my needs, so I returned to using Copilot, which has since been improved with the addition of a well-designed agent. Ultimately, integrating the agent into the IDE proved superior to CLI-based tools.

### GitHub Copilot
GitHub Copilot was originally conceived as an IDE extension. It works effectively as a plugin in both IntelliJ and 
Visual Studio Code, providing a specialized programming chat that can anticipate a developer’s intentions and suggest 
entire code snippets. After two years of working with Copilot, I can confidently say that I have saved 40% to 70% 
of the time compared to the basic autocomplete features IDEs offered before the advent of AI.

**Update may 2025**

With the addition of the edit function and, later, the agent, Copilot has become a highly practical and easy-to-use tool. In the Visual Studio Code version, it can be further enhanced with a wide range of extensions and MCP servers.

The time savings are tangible. Copilot enables faster progress and clearer thinking. Creativity and strategy are enhanced, but the main challenge is breaking old habits to adopt new ways of thinking and working.

### Vibe Coding

see [Vibe Coding Section](./vibe-coding/README.md) for more details. 

### Prompt Engineering

Prompt engineering is new discipline that emerges from the enhanced capabilities of services based on LLMs to understand natural languages and correctly 
interpret the context of a request. In this regard, [Prompt Engineering Guide](https://www.promptingguide.ai/) offers an excellent guide for those who 
want to venture into this new profession.

See [Prompt Engineering Section](prompts/prompts.md) for examples.
