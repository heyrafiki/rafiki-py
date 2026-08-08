from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.webhook_endpoint_input_events_item import (
    WebhookEndpointInputEventsItem,
    check_webhook_endpoint_input_events_item,
)

T = TypeVar("T", bound="WebhookEndpointInput")


@_attrs_define
class WebhookEndpointInput:
    url: str
    events: list[WebhookEndpointInputEventsItem]

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        events = []
        for events_item_data in self.events:
            events_item: str = events_item_data
            events.append(events_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
                "events": events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = check_webhook_endpoint_input_events_item(events_item_data)

            events.append(events_item)

        webhook_endpoint_input = cls(
            url=url,
            events=events,
        )

        return webhook_endpoint_input
