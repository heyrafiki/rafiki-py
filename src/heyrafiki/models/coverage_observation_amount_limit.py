from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.coverage_observation_amount_limit_currency import (
    CoverageObservationAmountLimitCurrency,
    check_coverage_observation_amount_limit_currency,
)

T = TypeVar("T", bound="CoverageObservationAmountLimit")


@_attrs_define
class CoverageObservationAmountLimit:
    currency: CoverageObservationAmountLimitCurrency
    value: int

    def to_dict(self) -> dict[str, Any]:
        currency: str = self.currency

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "currency": currency,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = check_coverage_observation_amount_limit_currency(d.pop("currency"))

        value = d.pop("value")

        coverage_observation_amount_limit = cls(
            currency=currency,
            value=value,
        )

        return coverage_observation_amount_limit
