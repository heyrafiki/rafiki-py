from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.claim import Claim


T = TypeVar("T", bound="ClaimList")


@_attrs_define
class ClaimList:
    object_: Literal["list"]
    data: list[Claim]
    has_more: bool

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        has_more = self.has_more

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "data": data,
                "has_more": has_more,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.claim import Claim

        d = dict(src_dict)
        object_ = cast(Literal["list"], d.pop("object"))
        if object_ != "list":
            raise ValueError(f"object must match const 'list', got '{object_}'")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Claim.from_dict(data_item_data)

            data.append(data_item)

        has_more = d.pop("has_more")

        claim_list = cls(
            object_=object_,
            data=data,
            has_more=has_more,
        )

        return claim_list
