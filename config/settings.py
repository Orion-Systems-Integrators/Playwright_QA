from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

try:
    from dotenv import load_dotenv
    BASE_DIR = Path(__file__).resolve().parent.parent
    load_dotenv(BASE_DIR / ".env")
except ImportError:
    BASE_DIR = Path(__file__).resolve().parent.parent
    print("Warning: python-dotenv not installed. Using environment variables or defaults.")


@dataclass(frozen=True)
class Settings:
    base_url: str
    username: str
    password: str


def get_settings() -> Settings:
    return Settings(
        base_url=os.getenv("BASE_URL", "https://www.saucedemo.com"),
        username=os.getenv("VALID_USERNAME", "standard_user"),
        password=os.getenv("VALID_PASSWORD", "secret_sauce"),
    )
