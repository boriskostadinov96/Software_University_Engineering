from unittest import TestCase, main
from collections import deque

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.railway = RailwayStation("Sofia")

    def test_correct_init(self):
        self.assertEqual("Sofia", self.railway.name)
        self.assertEqual(deque(), self.railway.arrival_trains)
        self.assertEqual(deque(), self.railway.departure_trains)

    def test_name_with_less_than_three_characters_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.railway.name = "bb"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_name_with_three_characters_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.railway.name = "asd"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board(self):
        self.assertEqual(len(self.railway.arrival_trains), 0)
        self.assertEqual(self.railway.arrival_trains, deque())

        self.railway.new_arrival_on_board("Some info")

        self.assertEqual(len(self.railway.arrival_trains), 1)
        self.assertEqual(self.railway.arrival_trains, deque(["Some info"]))

    def test_train_has_arrived_other_trains(self):
        self.railway.new_arrival_on_board("Some info")

        self.assertEqual(len(self.railway.arrival_trains), 1)
        self.assertEqual(len(self.railway.departure_trains), 0)

        train_info = "Some info 2"
        result = self.railway.train_has_arrived(train_info)
        expected_message = f"There are other trains to arrive before {train_info}."
        self.assertEqual(result, expected_message)

        self.assertEqual(len(self.railway.arrival_trains), 1)
        self.assertEqual(len(self.railway.departure_trains), 0)

    def test_train_has_arrived_go_to_departure(self):
        self.railway.new_arrival_on_board("Some info")

        self.assertEqual(len(self.railway.arrival_trains), 1)
        self.assertEqual(len(self.railway.departure_trains), 0)

        train_info = "Some info"
        result = self.railway.train_has_arrived(train_info)
        expected_message = f"{train_info} is on the platform and will leave in 5 minutes."
        self.assertEqual(result, expected_message)

        self.assertEqual(len(self.railway.arrival_trains), 0)
        self.assertEqual(len(self.railway.departure_trains), 1)

    def test_train_has_left_no_departure_trains(self):
        self.railway.new_arrival_on_board("Some info")

        self.assertEqual(len(self.railway.arrival_trains), 1)
        self.assertEqual(len(self.railway.departure_trains), 0)

        result = self.railway.train_has_left("Some info")
        self.assertFalse(result)

    def test_train_has_left_same_info(self):
        self.railway.new_arrival_on_board("Some info")
        self.railway.train_has_arrived("Some info")

        self.assertEqual(len(self.railway.departure_trains), 1)
        self.assertEqual(len(self.railway.arrival_trains), 0)

        result = self.railway.train_has_left("Some info")
        self.assertTrue(result)

        self.assertEqual(len(self.railway.departure_trains), 0)
        self.assertEqual(len(self.railway.arrival_trains), 0)

        self.assertEqual(self.railway.departure_trains, deque())

    def test_train_has_left_different_info(self):
        self.railway.new_arrival_on_board("Some info")
        self.railway.train_has_arrived("Some info")

        self.assertEqual(len(self.railway.departure_trains), 1)
        self.assertEqual(len(self.railway.arrival_trains), 0)

        result = self.railway.train_has_left("Other info")
        self.assertFalse(result)

        self.assertEqual(len(self.railway.departure_trains), 1)
        self.assertEqual(len(self.railway.arrival_trains), 0)


if __name__ == "__main__":
    main()
