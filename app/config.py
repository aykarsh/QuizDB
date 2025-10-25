"""Application configuration helpers."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class DatabaseConfig:
    host: str = os.getenv("FSDU3_DB_HOST", "localhost")
    port: int = int(os.getenv("FSDU3_DB_PORT", "3306"))
    user: str = os.getenv("FSDU3_DB_USER", "akarsh")
    password: str = os.getenv("FSDU3_DB_PASSWORD", "Akar$h1312")
    database: str = os.getenv("FSDU3_DB_NAME", "fsdu3")


def get_db_config() -> DatabaseConfig:
    """Return database configuration loaded from environment."""
    return DatabaseConfig()
