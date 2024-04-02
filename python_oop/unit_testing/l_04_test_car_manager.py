from unittest import TestCase, main

from l_04_car_manager import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("BMW", "E4", 15, 5000)

    def test_correct_init(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("E4", self.car.model)
        self.assertEqual(15, self.car.fuel_consumption)
        self.assertEqual(5000, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_cannot_be_empty_string_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_cannot_be_empty_string_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_with_zero_and_negative_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = - 3

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_zero_and_negative_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = - 3

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_cannot_be_negative_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = - 7

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_zero_and_negative_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-3)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive_with_not_enough_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_enough_fuel(self):
        self.car.refuel(1000)
        self.car.drive(100)
        self.assertEqual(985, self.car.fuel_amount)


if __name__ == "__main__":
    main()
