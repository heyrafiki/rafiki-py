from __future__ import annotations

import datetime


def parse_datetime(value: str) -> datetime.datetime:
    """Parse an RFC 3339 timestamp on every supported Python version."""
    if value.endswith("Z"):
        value = f"{value[:-1]}+00:00"
    return datetime.datetime.fromisoformat(value)
