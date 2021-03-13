from datetime import timedelta

from traffic_signaling.problem.street_plan import StreetPlan, Intersection, Street
from traffic_signaling.problem.car_path import CarPath


class TrafficSignalingProblemLoader:
    def __init__(self, input_file_path):
        self._input_file_path = input_file_path

    def get_simulation_duration(self):
        with open(self._input_file_path, "r") as data_file:
            first_row = data_file.readline().strip()
            return timedelta(seconds=int(first_row.split(sep=" ")[0]))

    def get_streetplan(self):
        with open(self._input_file_path, "r") as data_file:
            first_row = data_file.readline().strip().split(sep=" ")
            n_intersections, n_streets = int(first_row[1]), int(first_row[2])

        intersections = self._get_intersections(n_intersections)
        streets = self._get_streets(n_streets, intersections=intersections)

        return StreetPlan(intersections=intersections, streets=streets)

    def _get_intersections(self, n_intersections):
        return {
            Intersection(intersection_id=intersection_id)
            for intersection_id in range(n_intersections)
        }

    def _get_streets(self, n_streets, intersections):
        insersection_id_to_intersection = {intersection.intersection_id: intersection for intersection in intersections}
        streets = []
        with open(self._input_file_path, "r") as data_file:
            for row in list(data_file)[1 : n_streets + 1]:
                (
                    intersection1,
                    intersection2,
                    street_name,
                    traverse_time,
                ) = row.strip().split(sep=" ")
                street = Street(
                    intersection1=insersection_id_to_intersection[int(intersection1)],
                    intersection2=insersection_id_to_intersection[int(intersection2)],
                    street_name=street_name,
                    traverse_time=timedelta(seconds=int(traverse_time)),
                )
                streets.append(street)
        return streets

    def get_demand(self):
        with open(self._input_file_path, "r") as data_file:
            first_row = data_file.readline().strip().split(sep=" ")
            n_streets, n_cars = int(first_row[2]), int(first_row[3])

        streetplan = self.get_streetplan()
        street_name_to_street = {street.street_name: street for street in streetplan.streets}
        demand = []
        with open(self._input_file_path, "r") as data_file:
            for row in list(data_file)[n_streets + 1 : n_streets + n_cars + 1]:
                street_names_in_path = [street_name_to_street[street_name] for street_name in row.strip().split(sep=" ")[1:]]
                car_path = CarPath(streets_sequence=street_names_in_path)
                demand.append(car_path)

        return demand
