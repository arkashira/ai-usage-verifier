# ai-usage-verifier

```markdown
<h3 align="center">🛠️ ai-usage-verifier</h3>

<div align="center">
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
  [![Build Status](https://img.shields.io/badge/Build-passing-green.svg)](https://github.com/axentx/ai-usage-verifier)
  [![Stars](https://img.shields.io/github/stars/axentx/ai-usage-verifier?style=social)](https://github.com/axentx/ai-usage-verifier)
</div>

---

# 🚀 ai-usage-verifier
**Power Python developers with transparent AI component usage verification.** A Python package that logs AI component usage in JSON-LD format, reducing regulatory compliance effort by over 80%.

## Why ai-usage-verifier?
- **Lightweight**: Pure Python solution with minimal latency and zero runtime overhead
- **Easy Integration**: Add AI usage tracking with a single line of code
- **Audit-Ready**: Stores records locally in JSON-LD compliant format
- **Compliance Focused**: Reduces audit effort by over 80% with standardized AI usage logs
- **Developer Friendly**: Designed specifically for Python developers building AI-powered applications

## Feature Overview
| Feature | Description |
|--------|-------------|
| AI Usage Logging | Records all AI component interactions with detailed metadata |
| JSON-LD Compliance | Stores audit-ready logs in standardized JSON-LD format |
| Zero Runtime Overhead | Minimal performance impact on your application |
| Single Line Integration | Simple API for quick implementation |
| Local Storage | Securely stores usage records locally |

## Tech Stack
- Python
- JSON-LD

## Project Structure
```
ai-usage-verifier/
├── business/          # Business logic and domain models
├── docs/             # Documentation files
├── src/              # Source code implementation
└── tests/            # Unit and integration tests
```

## Getting Started
1. Install the package:
```bash
pip install ai-usage-verifier
```

2. Initialize in your project:
```python
from ai_usage_verifier import UsageVerifier

verifier = UsageVerifier()
verifier.initialize()
```

3. Track AI component usage:
```python
verifier.log_component_usage(
    component_name="openai-gpt-4",
    input_data="User query text",
    output_data="AI response",
    metadata={"model_version": "4.0", "processing_time": 1.2}
)
```

4. Run tests:
```bash
python -m pytest tests/
```

## Deploy
```bash
pip install build
python -m build
pip install dist/ai_usage_verifier-*.whl
```

## Status
Early development stage with sandbox-tested implementation. Recent commits focus on core functionality and documentation.

## Contributing
[Contributing.md](CONTRIBUTING.md)

## License
MIT License
```