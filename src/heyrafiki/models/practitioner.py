from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.practitioner_location import PractitionerLocation
    from ..models.practitioner_session_fee import PractitionerSessionFee


T = TypeVar("T", bound="Practitioner")


@_attrs_define
class Practitioner:
    id: str
    object_: Literal["practitioner"]
    name: str
    profession: str
    location: PractitionerLocation
    session_fee: PractitionerSessionFee

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        object_ = self.object_

        name = self.name

        profession = self.profession

        location = self.location.to_dict()

        session_fee = self.session_fee.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "object": object_,
                "name": name,
                "profession": profession,
                "location": location,
                "session_fee": session_fee,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.practitioner_location import PractitionerLocation
        from ..models.practitioner_session_fee import PractitionerSessionFee

        d = dict(src_dict)
        id = d.pop("id")

        object_ = cast(Literal["practitioner"], d.pop("object"))
        if object_ != "practitioner":
            raise ValueError(f"object must match const 'practitioner', got '{object_}'")

        name = d.pop("name")

        profession = d.pop("profession")

        location = PractitionerLocation.from_dict(d.pop("location"))

        session_fee = PractitionerSessionFee.from_dict(d.pop("session_fee"))

        practitioner = cls(
            id=id,
            object_=object_,
            name=name,
            profession=profession,
            location=location,
            session_fee=session_fee,
        )

        return practitioner
