from datetime import timedelta
from typing import Iterable

from traffic_signaling.problem.trafic_signaling_problem_loader import (
    TrafficSignalingProblemLoader,
)


class TrafficSignalingProblem:
    def __init__(
        self,
        simulation_duration: timedelta,
        streetplan: StreetPlan,
        demand: Iterable[CarPath],
    ):
        self._simulation_duration = simulation_duration
        self._streetplan = streetplan
        self._demand = demand

    @classmethod
    def from_file(cls, input_file):
        tsp_loader = TrafficSignalingProblemLoader(input_file=input_file)
        return cls(
            simulation_duration=tsp_loader.get_simulation_duration(),
            streetplan=tsp_loader.get_streetplan(),
            demand=tsp_loader.get_demand(),
        )
