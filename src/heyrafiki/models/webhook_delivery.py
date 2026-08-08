from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebhookDelivery")


@_attrs_define
class WebhookDelivery:
    id: str
    object_: Literal["webhook_delivery"]
    delivered: bool
    attempts: int
    response_status: int | None

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        object_ = self.object_

        delivered = self.delivered

        attempts = self.attempts

        response_status: int | None
        response_status = self.response_status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "object": object_,
                "delivered": delivered,
                "attempts": attempts,
                "response_status": response_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        object_ = cast(Literal["webhook_delivery"], d.pop("object"))
        if object_ != "webhook_delivery":
            raise ValueError(f"object must match const 'webhook_delivery', got '{object_}'")

        delivered = d.pop("delivered")

        attempts = d.pop("attempts")

        def _parse_response_status(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        response_status = _parse_response_status(d.pop("response_status"))

        webhook_delivery = cls(
            id=id,
            object_=object_,
            delivered=delivered,
            attempts=attempts,
            response_status=response_status,
        )

        return webhook_delivery
