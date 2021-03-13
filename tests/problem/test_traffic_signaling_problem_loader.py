from datetime import timedelta
import pytest

from traffic_signaling.problem.traffic_signaling_problem_loader import (
    TrafficSignalingProblemLoader,
)
from traffic_signaling.problem.street_plan import StreetPlan
from traffic_signaling.problem.car_path import CarPath


@pytest.fixture
def tsp_loader():
    return TrafficSignalingProblemLoader(input_file_path="./data/hashcode.in")


@pytest.fixture
def streetplan(tsp_loader):
    return tsp_loader.get_streetplan()


@pytest.fixture
def demand(tsp_loader):
    return tsp_loader.get_demand()


def test_initialize_tsp_loader(tsp_loader):
    return True


def test_get_simulation_duration(tsp_loader):
    assert tsp_loader.get_simulation_duration() == timedelta(seconds=7071)


def test_get_streetplan(streetplan):
    assert isinstance(streetplan, StreetPlan)

    assert len(streetplan.intersections) == 8000
    assert len(streetplan.streets) == 63968


def test_streetplan_intersections(streetplan):
    assert all(
        street.intersection1 in streetplan.intersections
        and street.intersection2 in streetplan.intersections
        for street in streetplan.streets
    )


def test_streetplan_traverse_times(streetplan):
    assert all(
        isinstance(street.traverse_time, timedelta)
        and street.traverse_time > timedelta(0)
        for street in streetplan.streets
    )


def test_get_demand(demand):
    assert all(isinstance(car_path, CarPath) for car_path in demand)
    assert len(demand) == 1000
    assert demand[0].get_n_streets() == 120
    assert [street.street_name for street in demand[0].streets_sequence][:3] == ["fifd-bebc", "bebc-gf", "gf-baah"]
    assert [street.street_name for street in demand[-1].streets_sequence][:3] == ["ddhg-bjh", "bjh-de", "de-ddgc"]

