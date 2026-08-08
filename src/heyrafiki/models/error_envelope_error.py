from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ErrorEnvelopeError")


@_attrs_define
class ErrorEnvelopeError:
    code: str
    message: str
    docs: str

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        docs = self.docs

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "message": message,
                "docs": docs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        docs = d.pop("docs")

        error_envelope_error = cls(
            code=code,
            message=message,
            docs=docs,
        )

        return error_envelope_error
