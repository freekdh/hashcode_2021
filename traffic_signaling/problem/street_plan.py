from dataclasses import dataclass
from datetime import timedelta
from typing import Iterable


@dataclass(frozen=True, eq=True)
class Intersection:
    intersection_id: int


@dataclass(frozen=True, eq=True)
class Street:
    intersection1: Intersection
    intersection2: Intersection
    street_name: str
    traverse_time: timedelta


class StreetPlan:
    def __init__(
        self, intersections: Iterable[Intersection], streets: Iterable[Street]
    ):
        self._intersections = set(intersections)
        self._streets = set(streets)

    @property
    def intersections(self):
        return self._intersections

    @property
    def streets(self):
        return self._streets
