from datetime import timedelta

from traffic_signaling.problem.street_plan import Intersection, Street


def test_intersection():
    assert Intersection(intersection_id=1) == Intersection(intersection_id=1)
    assert len(set([Intersection(1), Intersection(1)])) == 1
    assert len(set([Intersection(1), Intersection(2)])) == 2


def test_street():
    assert Street(
        intersection1=Intersection(1),
        intersection2=Intersection(2),
        street_name="foo",
        traverse_time=timedelta(seconds=10),
    ) == Street(
        intersection1=Intersection(1),
        intersection2=Intersection(2),
        street_name="foo",
        traverse_time=timedelta(seconds=10),
    )
