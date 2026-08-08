from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PreauthorizationDecisionPolicy")


@_attrs_define
class PreauthorizationDecisionPolicy:
    reference: str
    version: str

    def to_dict(self) -> dict[str, Any]:
        reference = self.reference

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "reference": reference,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reference = d.pop("reference")

        version = d.pop("version")

        preauthorization_decision_policy = cls(
            reference=reference,
            version=version,
        )

        return preauthorization_decision_policy
