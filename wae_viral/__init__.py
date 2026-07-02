"""
WAE Viral Prediction Engine - Python SDK
Official client library for the WAE Viral Score API.

Usage:
    from wae_viral import WAEClient
    
    client = WAEClient(api_key="your-api-key")
    result = client.predict(
        animal="Lion",
        description="A majestic lion roaring at sunset",
        platform="instagram"
    )
    print(f"Viral Score: {result.score}/100 ({result.tier})")
"""

__version__ = "1.0.0"
__author__ = "WAE Media"

import requests
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Prediction:
    """Viral score prediction result."""
    score: int
    tier: str
    confidence: str
    triggers: List[str]
    recommendations: List[str]
    platform: str
    animal: str


@dataclass  
class GeneratedContent:
    """Generated content result."""
    video_prompt: str
    caption: str
    hashtags: List[str]
    viral_score: int


class WAEClient:
    """Official Python client for WAE Viral Prediction Engine API."""
    
    BASE_URL = "https://ai.wildanimalencounter.com/api"
    
    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        """
        Initialize WAE API client.
        
        Args:
            api_key: Your WAE API key (optional for free tier)
            base_url: Custom API base URL (default: https://ai.wildanimalencounter.com/api)
        """
        self.api_key = api_key
        self.base_url = base_url or self.BASE_URL
        self.session = requests.Session()
        if api_key:
            self.session.headers["Authorization"] = f"Bearer {api_key}"
        self.session.headers["Content-Type"] = "application/json"
        self.session.headers["User-Agent"] = f"wae-viral-sdk/{__version__}"
    
    def predict(self, animal: str, description: str, platform: str = "instagram") -> Prediction:
        """
        Predict viral score for content.
        
        Args:
            animal: The animal subject (e.g., "Lion", "Eagle")
            description: Content description/caption
            platform: Target platform (instagram, tiktok, facebook, youtube)
            
        Returns:
            Prediction object with score, tier, triggers, and recommendations
            
        Raises:
            WAEAPIError: If the API returns an error
        """
        response = self.session.post(
            f"{self.base_url}/score",
            json={
                "animal": animal,
                "description": description,
                "platform": platform
            }
        )
        
        if response.status_code == 429:
            raise WAERateLimitError("Rate limit exceeded. Please wait before retrying.")
        
        data = response.json()
        
        if not data.get("success"):
            raise WAEAPIError(data.get("error", "Unknown API error"))
        
        pred = data["prediction"]
        return Prediction(
            score=pred["score"],
            tier=pred["tier"],
            confidence=pred.get("confidence", "N/A"),
            triggers=pred.get("triggers", []),
            recommendations=pred.get("recommendations", []),
            platform=platform,
            animal=animal
        )
    
    def generate(self, animal: str, platform: str = "instagram", style: str = "engaging") -> GeneratedContent:
        """
        Generate optimized content for an animal.
        
        Args:
            animal: The animal subject
            platform: Target platform
            style: Content style (engaging, educational, dramatic)
            
        Returns:
            GeneratedContent with video prompt, caption, hashtags, and predicted score
        """
        response = self.session.post(
            f"{self.base_url}/generate",
            json={
                "animal": animal,
                "platform": platform,
                "style": style
            }
        )
        
        data = response.json()
        
        if not data.get("success"):
            raise WAEAPIError(data.get("error", "Unknown API error"))
        
        gen = data["generated"]
        return GeneratedContent(
            video_prompt=gen.get("video_prompt", ""),
            caption=gen.get("caption", ""),
            hashtags=gen.get("hashtags", []),
            viral_score=gen.get("viral_score", 0)
        )
    
    def analyze(self, description: str, platform: str = "instagram") -> dict:
        """
        Deep analysis of content performance factors.
        
        Args:
            description: Content to analyze
            platform: Target platform
            
        Returns:
            Dictionary with detailed analysis results
        """
        response = self.session.post(
            f"{self.base_url}/analyze",
            json={
                "description": description,
                "platform": platform
            }
        )
        
        data = response.json()
        if not data.get("success"):
            raise WAEAPIError(data.get("error", "Unknown API error"))
        
        return data.get("analysis", {})


class WAEAPIError(Exception):
    """Base exception for WAE API errors."""
    pass


class WAERateLimitError(WAEAPIError):
    """Raised when API rate limit is exceeded."""
    pass
