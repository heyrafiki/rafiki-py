from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ClaimLine")


@_attrs_define
class ClaimLine:
    line_number: int
    code_system: str
    code_system_version: None | str
    service_code: str
    units: float
    amount: int

    def to_dict(self) -> dict[str, Any]:
        line_number = self.line_number

        code_system = self.code_system

        code_system_version: None | str
        code_system_version = self.code_system_version

        service_code = self.service_code

        units = self.units

        amount = self.amount

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "line_number": line_number,
                "code_system": code_system,
                "code_system_version": code_system_version,
                "service_code": service_code,
                "units": units,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line_number = d.pop("line_number")

        code_system = d.pop("code_system")

        def _parse_code_system_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        code_system_version = _parse_code_system_version(d.pop("code_system_version"))

        service_code = d.pop("service_code")

        units = d.pop("units")

        amount = d.pop("amount")

        claim_line = cls(
            line_number=line_number,
            code_system=code_system,
            code_system_version=code_system_version,
            service_code=service_code,
            units=units,
            amount=amount,
        )

        return claim_line
