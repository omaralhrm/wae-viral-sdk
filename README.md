# WAE Viral Score SDK

[![PyPI version](https://badge.fury.io/py/wae-viral-sdk.svg)](https://pypi.org/project/wae-viral-sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**Official Python SDK for the WAE Viral Prediction Engine** — Predict content virality before posting, built on 833M+ first-party organic views primarily documented through official Meta/Facebook/Instagram analytics exports.

## Installation

```bash
pip install wae-viral-sdk
```

Or install from source:

```bash
git clone https://github.com/omaralhrm/wae-viral-sdk.git
cd wae-viral-sdk
pip install -e .
```

## Quick Start

```python
from wae_viral import WAEClient

# Initialize client
client = WAEClient(api_key="your-api-key")

# Predict viral score
result = client.predict(
    animal="Lion",
    description="A majestic lion roaring at golden hour sunset in the Serengeti",
    platform="instagram"
)

print(f"Viral Score: {result.score}/100")
print(f"Tier: {result.tier}")
print(f"Triggers: {result.triggers}")
print(f"Recommendations: {result.recommendations}")
```

## Features

| Feature | Description |
|---------|-------------|
| **Viral Prediction** | Score content 0-100 before posting |
| **Content Generation** | AI-generated captions and hashtags |
| **Multi-Platform** | Instagram, Facebook (Meta platforms) |
| **Trigger Analysis** | Identify what makes content go viral |
| **Recommendations** | Actionable tips to boost engagement |

## API Methods

### `client.predict(animal, description, platform)`

Predict viral score for content.

```python
result = client.predict(
    animal="Eagle",
    description="Bald eagle catching fish mid-flight",
    platform="instagram"
)
# Returns: Prediction(score=87, tier="Viral", triggers=["action_shot", "rare_moment"], ...)
```

### `client.generate(animal, platform, style)`

Generate optimized content for an animal.

```python
content = client.generate(
    animal="Wolf",
    platform="instagram",
    style="dramatic"
)
print(content.caption)
print(content.hashtags)
print(f"Predicted score: {content.viral_score}")
```

### `client.analyze(description, platform)`

Deep analysis of content performance factors.

```python
analysis = client.analyze(
    description="Baby elephant playing in mud with its mother",
    platform="facebook"
)
```

## Supported Platforms

- Instagram (Reels, Posts, Stories)
- Facebook (Reels, Posts, Videos)

> **Note:** Current verified dataset primarily documents Meta/Facebook/Instagram records. Additional platforms (YouTube, TikTok) may be added in future versions.

## Error Handling

```python
from wae_viral import WAEClient, WAEAPIError, WAERateLimitError

client = WAEClient(api_key="your-key")

try:
    result = client.predict(animal="Lion", description="...", platform="instagram")
except WAERateLimitError:
    print("Rate limit hit - wait before retrying")
except WAEAPIError as e:
    print(f"API Error: {e}")
```

## Links

- **Live Demo:** https://ai.wildanimalencounter.com
- **API Docs:** https://ai.wildanimalencounter.com/api-docs
- **Model Card:** https://huggingface.co/OmarWAEMedia/WAE-Viral-Score-Engine-v1
- **Company:** https://wildanimalencounter.com

## License

MIT License - see [LICENSE](LICENSE) for details.

---

*Built by [WAE Media](https://wildanimalencounter.com) — AI-Native Media Intelligence*
