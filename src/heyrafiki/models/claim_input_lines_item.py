from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClaimInputLinesItem")


@_attrs_define
class ClaimInputLinesItem:
    code_system: str
    service_code: str
    units: float
    amount: int
    code_system_version: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code_system = self.code_system

        service_code = self.service_code

        units = self.units

        amount = self.amount

        code_system_version: None | str | Unset
        if isinstance(self.code_system_version, Unset):
            code_system_version = UNSET
        else:
            code_system_version = self.code_system_version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code_system": code_system,
                "service_code": service_code,
                "units": units,
                "amount": amount,
            }
        )
        if code_system_version is not UNSET:
            field_dict["code_system_version"] = code_system_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code_system = d.pop("code_system")

        service_code = d.pop("service_code")

        units = d.pop("units")

        amount = d.pop("amount")

        def _parse_code_system_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code_system_version = _parse_code_system_version(d.pop("code_system_version", UNSET))

        claim_input_lines_item = cls(
            code_system=code_system,
            service_code=service_code,
            units=units,
            amount=amount,
            code_system_version=code_system_version,
        )

        return claim_input_lines_item
