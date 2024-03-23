class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):
    def test_is_worker_object_initialized_properly(self):
        # Act:
        worker = Worker("John", 1500, 90)

        # Assert
        self.assertEqual("John", worker.name)
        self.assertEqual(1500, worker.salary)
        self.assertEqual(90, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_works(self):
        #  Arrange
        worker = Worker("John", 1500, 90)
        self.assertEqual(0, worker.money)
        self.assertEqual(90, worker.energy)

        # Act
        worker.work()

        # Assert
        current_expected_money = 1500
        self.assertEqual(current_expected_money, worker.money)
        expected_energy = 90 - 1
        self.assertEqual(expected_energy, worker.energy)

        worker.work()
        # Worker work again
        current_expected_money = 1000 + 1000
        self.assertEqual(current_expected_money, worker.money)
        expected_energy = 60 - 1 - 1
        self.assertEqual(expected_energy, worker.energy)

    def test_worker_with_zero_energy(self):
        worker = Worker("John", 1500, 0)

        with self.assertRaises(Exception):
            worker.work()

    def test_worker_with_negative_energy(self):
        worker = Worker("John", 1500, -4)

        with self.assertRaises(Exception):
            worker.work()

    def test_worker_energy_increase_when_rests(self):
        # Arrange
        worker = Worker("John", 1500, 90)
        self.assertEqual(90, worker.energy)

        # Act
        worker.rest()
        self.assertEqual(91, worker.energy)

        worker.rest()
        self.assertEqual(92, worker.energy)

    def test_get_info(self):
        # Arrange
        worker = Worker("John", 1500, 90)

        # Act
        result = worker.get_info()

        # Assert
        expected_result = 'Test has saved 1500 money.'
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
