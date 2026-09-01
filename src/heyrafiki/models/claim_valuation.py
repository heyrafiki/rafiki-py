from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from .._compat import parse_datetime
from ..models.claim_valuation_status import ClaimValuationStatus, check_claim_valuation_status

if TYPE_CHECKING:
    from ..models.claim_valuation_amount import ClaimValuationAmount
    from ..models.claim_valuation_event import ClaimValuationEvent
    from ..models.claim_valuation_policy_type_0 import ClaimValuationPolicyType0


T = TypeVar("T", bound="ClaimValuation")


@_attrs_define
class ClaimValuation:
    id: str
    """ Stable composite of the Claim identifier and valuation cutoff. """
    object_: Literal["claim_valuation"]
    claim_id: str
    valuation_at: datetime.datetime
    currency: str
    status: ClaimValuationStatus
    amount: ClaimValuationAmount
    policy: ClaimValuationPolicyType0 | None
    events: list[ClaimValuationEvent]

    def to_dict(self) -> dict[str, Any]:
        from ..models.claim_valuation_policy_type_0 import ClaimValuationPolicyType0

        id = self.id

        object_ = self.object_

        claim_id = self.claim_id

        valuation_at = self.valuation_at.isoformat()

        currency = self.currency

        status: str = self.status

        amount = self.amount.to_dict()

        policy: dict[str, Any] | None
        if isinstance(self.policy, ClaimValuationPolicyType0):
            policy = self.policy.to_dict()
        else:
            policy = self.policy

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "object": object_,
                "claim_id": claim_id,
                "valuation_at": valuation_at,
                "currency": currency,
                "status": status,
                "amount": amount,
                "policy": policy,
                "events": events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.claim_valuation_amount import ClaimValuationAmount
        from ..models.claim_valuation_event import ClaimValuationEvent
        from ..models.claim_valuation_policy_type_0 import ClaimValuationPolicyType0

        d = dict(src_dict)
        id = d.pop("id")

        object_ = cast(Literal["claim_valuation"], d.pop("object"))
        if object_ != "claim_valuation":
            raise ValueError(f"object must match const 'claim_valuation', got '{object_}'")

        claim_id = d.pop("claim_id")

        valuation_at = parse_datetime(d.pop("valuation_at"))

        currency = d.pop("currency")

        status = check_claim_valuation_status(d.pop("status"))

        amount = ClaimValuationAmount.from_dict(d.pop("amount"))

        def _parse_policy(data: object) -> ClaimValuationPolicyType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                policy_type_0 = ClaimValuationPolicyType0.from_dict(data)

                return policy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ClaimValuationPolicyType0 | None, data)

        policy = _parse_policy(d.pop("policy"))

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = ClaimValuationEvent.from_dict(events_item_data)

            events.append(events_item)

        claim_valuation = cls(
            id=id,
            object_=object_,
            claim_id=claim_id,
            valuation_at=valuation_at,
            currency=currency,
            status=status,
            amount=amount,
            policy=policy,
            events=events,
        )

        return claim_valuation
