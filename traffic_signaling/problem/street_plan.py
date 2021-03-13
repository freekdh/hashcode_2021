from dataclasses import dataclass
from datetime import timedelta
from typing import Iterable
import networkx as nx

@dataclass(frozen=True, eq=True)
class Intersection:
    intersection_id: int

    def __repr__(self):
        return f"Intersection {self.intersection_id}"


@dataclass(frozen=True, eq=True)
class Street:
    intersection1: Intersection
    intersection2: Intersection
    street_name: str
    traverse_time: timedelta

    def __repr__(self):
        return f"[{self.intersection1} <-> {self.intersection2}]"

class StreetPlan:
    def __init__(
        self, intersections: Iterable[Intersection], streets: Iterable[Street]
    ):
        self._intersections = set(intersections)
        self._streets = set(streets)

        self._graph = nx.DiGraph([street.intersection1, street.intersection2] for street in self._streets)

    @property
    def intersections(self):
        return self._intersections

    @property
    def streets(self):
        return self._streets

    @property
    def graph(self):
        return self._graph