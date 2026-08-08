from typing import Literal

WebhookEndpointWithSecretStatus = Literal["active", "disabled"]

WEBHOOK_ENDPOINT_WITH_SECRET_STATUS_VALUES: set[WebhookEndpointWithSecretStatus] = {
    "active",
    "disabled",
}


def check_webhook_endpoint_with_secret_status(value: str) -> WebhookEndpointWithSecretStatus:
    if value in WEBHOOK_ENDPOINT_WITH_SECRET_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEBHOOK_ENDPOINT_WITH_SECRET_STATUS_VALUES!r}"
    )
