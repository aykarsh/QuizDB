"""Database connection utilities for the quiz app."""

from __future__ import annotations

import contextlib
from typing import Iterator, Optional

import mysql.connector
from mysql.connector.connection import MySQLConnection

from .config import get_db_config


@contextlib.contextmanager
def get_connection(overrides: Optional[dict[str, str]] = None) -> Iterator[MySQLConnection]:
    """Yield a MySQL connection using project defaults."""
    cfg = get_db_config()
    params = {
        "host": overrides.get("host", cfg.host) if overrides else cfg.host,
        "port": overrides.get("port", cfg.port) if overrides else cfg.port,
        "user": overrides.get("user", cfg.user) if overrides else cfg.user,
        "password": overrides.get("password", cfg.password) if overrides else cfg.password,
        "database": overrides.get("database", cfg.database) if overrides else cfg.database,
    }
    connection = mysql.connector.connect(**params)
    try:
        yield connection
    finally:
        connection.close()


def execute_script(sql: str) -> None:
    """Execute a multi-statement SQL script."""
    with get_connection() as conn:
        cursor = conn.cursor()
        try:
            for statement in filter(None, (stmt.strip() for stmt in sql.split(";"))):
                cursor.execute(statement)
            conn.commit()
        finally:
            cursor.close()
