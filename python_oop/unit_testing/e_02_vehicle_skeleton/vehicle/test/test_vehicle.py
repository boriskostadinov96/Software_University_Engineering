from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(
            100,
            100
        )

    def test__init__method(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test_correct_value_for_class_attribute(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_without_fuel_raises_exception(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel(self):
        self.vehicle.drive(10)

        self.assertEqual(87.5, self.vehicle.fuel)

    def test_refuel_with_more_fuel_than_capacity_we_have(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1000)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_correct_amount(self):
        self.vehicle.fuel = 50

        self.vehicle.refuel(50)

        self.assertEqual(100, self.vehicle.fuel)

    def test__str__method(self):
        expected_result = "The vehicle has 100 horse power with 100 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected_result, self.vehicle.__str__())


if __name__ == "__main__":
    main()
