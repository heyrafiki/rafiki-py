# Changelog

## 0.1.0b2 - 2026-08-28

- Added typed sync and async operations for `GET /claims/{claim_id}/valuation` (`getClaimValuation`) with historical cutoff parameter `valuation_at`.
- Updated embedded OpenAPI contract snapshot to the canonical 31-operation definition.
- Added deterministic fixture-driven tests and models for reproducible Claim valuations.

## Contract 1.0 - 2026-08-10

- Added the Python SDK generated from the version 1 OpenAPI contract.
- Added typed sync and async operations for all 30 published endpoints.
- Added bounded retries for safe reads and caller-keyed writes.
- Added stable error handling with request identifiers.
- Added RFC 3339 timestamp parsing compatible with Python 3.10.
