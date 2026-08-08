from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.webhook_endpoint_status import WebhookEndpointStatus, check_webhook_endpoint_status

T = TypeVar("T", bound="WebhookEndpoint")


@_attrs_define
class WebhookEndpoint:
    id: str
    object_: Literal["webhook_endpoint"]
    url: str
    events: list[str]
    status: WebhookEndpointStatus
    created_at: datetime.datetime
    disabled_at: datetime.datetime | None

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        object_ = self.object_

        url = self.url

        events = self.events

        status: str = self.status

        created_at = self.created_at.isoformat()

        disabled_at: None | str
        if isinstance(self.disabled_at, datetime.datetime):
            disabled_at = self.disabled_at.isoformat()
        else:
            disabled_at = self.disabled_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "object": object_,
                "url": url,
                "events": events,
                "status": status,
                "created_at": created_at,
                "disabled_at": disabled_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        object_ = cast(Literal["webhook_endpoint"], d.pop("object"))
        if object_ != "webhook_endpoint":
            raise ValueError(f"object must match const 'webhook_endpoint', got '{object_}'")

        url = d.pop("url")

        events = cast(list[str], d.pop("events"))

        status = check_webhook_endpoint_status(d.pop("status"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_disabled_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                disabled_at_type_0 = datetime.datetime.fromisoformat(data)

                return disabled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        disabled_at = _parse_disabled_at(d.pop("disabled_at"))

        webhook_endpoint = cls(
            id=id,
            object_=object_,
            url=url,
            events=events,
            status=status,
            created_at=created_at,
            disabled_at=disabled_at,
        )

        return webhook_endpoint
