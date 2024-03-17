from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):

    def setUp(self) -> None:
        self.car = SecondHandCar("TestModel", "Tesla", 10000, 20000)

    def test_init(self):
        car = SecondHandCar("TestModel", "Tesla", 10000, 20000)
        self.assertEqual(car.model, "TestModel")
        self.assertEqual(car.car_type, "Tesla")
        self.assertEqual(car.mileage, 10000)
        self.assertEqual(car.price, 20000)
        self.assertEqual(car.repairs, [])
        self.assertListEqual(car.repairs, [])

    def test_price_less_than_one_or_equal_raises(self):
        with self.assertRaises(ValueError) as ex:
            car = SecondHandCar("TestModel", "Tesla", 10000, 1)
            self.assertEqual(str(ex.exception), "Price should be greater than 1.0!")

        with self.assertRaises(ValueError) as ex:
            car = SecondHandCar("TestModel", "Tesla", 10000, 0.9)
            self.assertEqual(str(ex.exception), "Price should be greater than 1.0!")

    def test_mileage_less_than_hundred_or_equal_raises(self):
        with self.assertRaises(ValueError) as ex:
            car = SecondHandCar("TestModel", "Tesla", 100, 20000)
            self.assertEqual(str(ex.exception), "Please, second-hand cars only! Mileage must be greater than 100!")

        with self.assertRaises(ValueError) as ex:
            car = SecondHandCar("TestModel", "Tesla", 98, 20000)
            self.assertEqual(str(ex.exception), "Please, second-hand cars only! Mileage must be greater than 100!")

    def test_set_promotional_price_higher_than_current_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(20000)
            self.assertEqual(str(ex.exception), 'You are supposed to decrease the price!')

        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(20001)
            self.assertEqual(str(ex.exception), 'You are supposed to decrease the price!')

    def test_set_promotional_price(self):
        self.assertEqual(self.car.price, 20000)

        result = self.car.set_promotional_price(10000)

        self.assertEqual(self.car.price, 10000)
        self.assertEqual(result, "The promotional price has been successfully set.")

    def test_repair_price_too_high_raises(self):
        self.assertEqual(self.car.price, 20000)
        self.assertEqual(self.car.repairs, [])
        half_price = self.car.price / 2

        result = self.car.need_repair(half_price + 1, "Test repair")

        self.assertEqual(result, "Repair is impossible!")
        self.assertEqual(self.car.price, 20000)
        self.assertEqual(self.car.repairs, [])

    def test_repair_exact_half_price(self):
        self.assertEqual(self.car.price, 20000)
        self.assertEqual(self.car.repairs, [])
        half_price = self.car.price / 2

        current_price = self.car.price

        result = self.car.need_repair(half_price, "Test repair")

        self.assertEqual(result, "Price has been increased due to repair charges.")
        self.assertEqual(self.car.price, current_price + half_price)
        self.assertEqual(self.car.repairs, ["Test repair"])

    def test_repair_less_than_half_price(self):
        self.assertEqual(self.car.price, 20000)
        self.assertEqual(self.car.repairs, [])
        half_price = self.car.price / 2 - 1

        current_price = self.car.price

        result = self.car.need_repair(half_price, "Test repair")

        self.assertEqual(result, "Price has been increased due to repair charges.")
        self.assertEqual(self.car.price, current_price + half_price)
        self.assertEqual(self.car.repairs, ["Test repair"])

    def test_compare_different_types_impossible(self):
        car2 = SecondHandCar("TestModel2", "Test2", 9000, 6700)

        result = car2 > self.car

        self.assertEqual(result, "Cars cannot be compared. Type mismatch!")

    def test_compare(self):
        car2 = SecondHandCar("TestModel2", self.car.car_type, 9000, 6700)

        result = car2 > self.car
        self.assertFalse(result)

    def test_str(self):
        self.assertEqual(str(self.car), "Model TestModel | Type Tesla | Milage 10000km\nCurrent price: 20000.00 | Number of Repairs: 0")


if __name__ == "__main__":
    main()
