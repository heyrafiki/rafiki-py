from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.coverage_observation import CoverageObservation


T = TypeVar("T", bound="CoverageBatchResult")


@_attrs_define
class CoverageBatchResult:
    object_: Literal["coverage_batch_result"]
    batch_reference: str
    artifact_sha256: str
    total: int
    recorded: int
    replayed: int
    observations: list[CoverageObservation]

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_

        batch_reference = self.batch_reference

        artifact_sha256 = self.artifact_sha256

        total = self.total

        recorded = self.recorded

        replayed = self.replayed

        observations = []
        for observations_item_data in self.observations:
            observations_item = observations_item_data.to_dict()
            observations.append(observations_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "batch_reference": batch_reference,
                "artifact_sha256": artifact_sha256,
                "total": total,
                "recorded": recorded,
                "replayed": replayed,
                "observations": observations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coverage_observation import CoverageObservation

        d = dict(src_dict)
        object_ = cast(Literal["coverage_batch_result"], d.pop("object"))
        if object_ != "coverage_batch_result":
            raise ValueError(f"object must match const 'coverage_batch_result', got '{object_}'")

        batch_reference = d.pop("batch_reference")

        artifact_sha256 = d.pop("artifact_sha256")

        total = d.pop("total")

        recorded = d.pop("recorded")

        replayed = d.pop("replayed")

        observations = []
        _observations = d.pop("observations")
        for observations_item_data in _observations:
            observations_item = CoverageObservation.from_dict(observations_item_data)

            observations.append(observations_item)

        coverage_batch_result = cls(
            object_=object_,
            batch_reference=batch_reference,
            artifact_sha256=artifact_sha256,
            total=total,
            recorded=recorded,
            replayed=replayed,
            observations=observations,
        )

        return coverage_batch_result
