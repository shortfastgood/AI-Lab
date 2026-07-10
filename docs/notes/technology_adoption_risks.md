# Technology adoption risks

AI presents substantial advantages, but it also introduces risks that require careful management. These threats differ from traditional cybersecurity concerns and demand revised controls and a higher level of operational awareness.

**Prompt injection** is a critical vulnerability in which adversaries embed instructions within apparently benign inputs in order to manipulate AI behaviour. A document submitted for analysis, for example, may contain hidden directives instructing a model to ignore safety constraints or to exfiltrate sensitive data.

**Jailbreaking** refers to techniques designed to bypass model safety mechanisms. Attackers use psychological and technical techniques to elicit disallowed outputs, reveal proprietary information or cause models to act outside their intended remit.

Other risks include data poisoning, in which training or fine-tuning data is corrupted to influence model behaviour, and model extraction, in which proprietary capabilities are probed and replicated. Organisations must also contend with hallucinations, privacy breaches and operational dependence on brittle models.

The [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) provides a useful framework for mitigation. For security-sensitive use‑cases, hosting models locally in protected environments is increasingly viable and can reduce exposure to data-leakage risks while preserving capability.

## Collateral Risks

Collateral risks are environmental and social in nature.

Among the social risks is the development of a systemic dependence on a small number of providers. The geopolitical risk associated with the decisions of those hosting these providers should not be overlooked.

Among the environmental risks are those associated with the vast resources consumed by large models. The concentration of demand around these models significantly increases the need for energy to operate them and for water to cool them, creating strain in places where these resources cannot be expanded at the same pace as the technology itself.
