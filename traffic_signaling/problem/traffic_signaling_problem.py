from datetime import timedelta
from typing import Iterable

from traffic_signaling.problem.traffic_signaling_problem_loader import (
    TrafficSignalingProblemLoader,
)
from traffic_signaling.problem.street_plan import StreetPlan
from traffic_signaling.problem.car_path import CarPath

class TrafficSignalingProblem:
    def __init__(
        self,
        simulation_duration: timedelta,
        carload_delivery_bonus_points: int,
        streetplan: StreetPlan,
        demand: Iterable[CarPath],
    ):
        self._simulation_duration = simulation_duration
        self._carload_delivery_bonus_points = carload_delivery_bonus_points
        self._streetplan = streetplan
        self._demand = demand

    @classmethod
    def from_file(cls, input_file_path):
        tsp_loader = TrafficSignalingProblemLoader(input_file_path=input_file_path)
        return cls(
            simulation_duration=tsp_loader.get_simulation_duration(),
            carload_delivery_bonus_points=tsp_loader.get_carload_delivery_bonus_points(),
            streetplan=tsp_loader.get_streetplan(),
            demand=tsp_loader.get_demand(),
        )

    @property
    def demand(self):
        return self._demand
    
    @property
    def streetplan(self):
        return self._streetplan
    
    @property
    def carload_delivery_bonus_points(self):
        return self._carload_delivery_bonus_points
    
    @property
    def simulation_duration(self):
        return self._simulation_duration