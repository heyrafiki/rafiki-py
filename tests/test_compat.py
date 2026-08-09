from __future__ import annotations

import datetime as dt

from heyrafiki._compat import parse_datetime


def test_parses_rfc_3339_utc_suffix() -> None:
    assert parse_datetime("2026-08-02T07:00:00.000Z") == dt.datetime(
        2026,
        8,
        2,
        7,
        tzinfo=dt.timezone.utc,
    )


def test_preserves_explicit_offset() -> None:
    assert parse_datetime("2026-08-02T10:00:00+03:00").utcoffset() == dt.timedelta(hours=3)
