from typing import Literal

WebhookEndpointStatus = Literal["active", "disabled"]

WEBHOOK_ENDPOINT_STATUS_VALUES: set[WebhookEndpointStatus] = {
    "active",
    "disabled",
}


def check_webhook_endpoint_status(value: str) -> WebhookEndpointStatus:
    if value in WEBHOOK_ENDPOINT_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEBHOOK_ENDPOINT_STATUS_VALUES!r}"
    )
