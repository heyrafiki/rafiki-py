from typing import Literal

WebhookEndpointInputEventsItem = Literal[
    "claim.approved",
    "claim.denied",
    "claim.information_requested",
    "claim.partially_approved",
    "claim.resubmitted",
    "claim.settled",
    "claim.submitted",
    "preauthorization.approved",
    "preauthorization.denied",
    "preauthorization.expired",
    "preauthorization.requested",
    "remittance.reconciled",
    "sandbox.ping",
]

WEBHOOK_ENDPOINT_INPUT_EVENTS_ITEM_VALUES: set[WebhookEndpointInputEventsItem] = {
    "claim.approved",
    "claim.denied",
    "claim.information_requested",
    "claim.partially_approved",
    "claim.resubmitted",
    "claim.settled",
    "claim.submitted",
    "preauthorization.approved",
    "preauthorization.denied",
    "preauthorization.expired",
    "preauthorization.requested",
    "remittance.reconciled",
    "sandbox.ping",
}


def check_webhook_endpoint_input_events_item(value: str) -> WebhookEndpointInputEventsItem:
    if value in WEBHOOK_ENDPOINT_INPUT_EVENTS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEBHOOK_ENDPOINT_INPUT_EVENTS_ITEM_VALUES!r}"
    )
