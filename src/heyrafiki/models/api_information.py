from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.api_information_environment import (
    ApiInformationEnvironment,
    check_api_information_environment,
)

T = TypeVar("T", bound="ApiInformation")


@_attrs_define
class ApiInformation:
    object_: Literal["api"]
    version: Literal["v1"]
    environment: ApiInformationEnvironment
    resources: list[str]

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_

        version = self.version

        environment: str = self.environment

        resources = self.resources

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "version": version,
                "environment": environment,
                "resources": resources,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = cast(Literal["api"], d.pop("object"))
        if object_ != "api":
            raise ValueError(f"object must match const 'api', got '{object_}'")

        version = cast(Literal["v1"], d.pop("version"))
        if version != "v1":
            raise ValueError(f"version must match const 'v1', got '{version}'")

        environment = check_api_information_environment(d.pop("environment"))

        resources = cast(list[str], d.pop("resources"))

        api_information = cls(
            object_=object_,
            version=version,
            environment=environment,
            resources=resources,
        )

        return api_information
