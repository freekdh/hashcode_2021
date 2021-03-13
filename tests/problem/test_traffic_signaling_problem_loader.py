from datetime import timedelta
import pytest

from traffic_signaling.problem.traffic_signaling_problem_loader import (
    TrafficSignalingProblemLoader,
)
from traffic_signaling.problem.street_plan import StreetPlan


@pytest.fixture
def tsp_loader():
    return TrafficSignalingProblemLoader(input_file_path="./data/hashcode.in")


@pytest.fixture
def streetplan(tsp_loader):
    return tsp_loader.get_streetplan()


def test_initialize_tsp_loader(tsp_loader):
    return True


def test_get_simulation_duration(tsp_loader):
    assert tsp_loader.get_simulation_duration() == timedelta(seconds=7071)


def test_get_streetplan(streetplan):
    assert isinstance(streetplan, StreetPlan)

    assert len(set(streetplan.intersections)) == 8000
    assert len(set(streetplan.streets)) == 63968


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
