### 🛠️ AI Usage Verifier

<div align="center">
  <a href="https://github.com/axentx/ai-usage-verifier">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
    <img src="https://img.shields.io/badge/Python-3.9-blue.svg" alt="Python 3.9">
    <img src="https://img.shields.io/badge/Build-Python%20setup%20script-blue.svg" alt="Build: Python setup script">
    <img src="https://img.shields.io/github/stars/axentx/ai-usage-verifier" alt="Stars: 0">
  </a>
</div>

---

# 🚀 AI Usage Verifier

**Power transparency with AI usage verification.** A lightweight Python library that lets developers record and verify AI components used within their software products.

## Why AI Usage Verifier?

* **Simplified AI component tracking**: Easily document and self-audit AI components in your codebase.
* **Transparency and trust**: Ensure transparency and trust among developers, marketers, and consumers.
* **Lightweight and in-memory**: No external services, databases, or complex analysis are performed.
* **Built for Python developers**: A simple solution for Python developers who need to verify AI usage.
* **Easy to integrate**: Minimal dependencies and a straightforward API.

## Feature Overview

| Feature | Description |
| --- | --- |
| `add_ai_usage` | Add AI usage records to the internal registry. |
| `get_ai_usage` | Retrieve AI usage records from the internal registry. |
| `verify_ai_usage` | Run basic validation checks on AI usage records. |
| `AIUsageVerifier` | A class that maintains an internal registry of AI usage entries. |

## Tech Stack

* Python

## Project Structure

```markdown
ai-usage-verifier/
business/
docs/
src/
tests/
README.md
pyproject.toml
requirements.txt
```

## Getting Started

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```
2. **Run the tests**:
```bash
pytest tests/
```
3. **Use the library**:
```python
from ai_usage_verifier import AIUsageVerifier

verifier = AIUsageVerifier()
verifier.add_ai_usage("component1")
verifier.add_ai_usage("component2")
print(verifier.get_ai_usage())
verifier.verify_ai_usage()
```

## Deploy

1. **Build the package**:
```bash
python setup.py sdist
```
2. **Upload to PyPI**:
```bash
twine upload dist/*
```

## Status

Last updated: 2026-06-20T10:05:59.910516Z
Recent commit: e6fe49f feat(ai-usage-verifier): real, sandbox-tested implementation

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to this project.

## License

AI Usage Verifier is licensed under the MIT License.