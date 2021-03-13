from dataclasses import dataclass
from typing import List

from traffic_signaling.problem.street_plan import Street


@dataclass(frozen=True, eq=False)
class CarPath:
    streets_sequence: List[Street]
