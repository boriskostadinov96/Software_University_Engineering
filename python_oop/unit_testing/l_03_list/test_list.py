from unittest import TestCase, main

from list import IntegerList


class TestInterList(TestCase):
    def setUp(self):
        self.integer_list = IntegerList(5.5, 1, 2, 3, "hello")

    def test_correct_init(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add_non_integer_element_to_the_list_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add(5.5)
            self.integer_list.add('asd')

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_integer_to_the_list(self):
        expected_list = self.integer_list.get_data() + [4]

        self.integer_list.add(4)

        self.assertEqual(expected_list, self.integer_list.get_data())

    def test_remove_index_that_is_out_of_range_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(100000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_valid_index_of_the_list(self):
        self.integer_list.remove_index(0)

        self.assertEqual([2, 3], self.integer_list.get_data())

    def test_get_index_that_is_out_of_range_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(10000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_valid_index(self):
        self.assertEqual(2, self.integer_list.get(1))

    def test_try_insert_element_to_index_out_of_range_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(10000, 4)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_non_integer_element_raises_index_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(1, 4.5)
            self.integer_list.insert(1, 'asd')

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_valid_element_to_a_valid_index(self):
        expected_list = self.integer_list.get_data().copy()

        expected_list.insert(1, 5)
        self.integer_list.insert(1, 5)

        self.assertEqual(expected_list, self.integer_list.get_data())

    def test_get_the_biggest_value_in_the_list(self):
        expected_biggest_value = max(self.integer_list.get_data())
        biggest_value = self.integer_list.get_biggest()

        self.assertEqual(expected_biggest_value, biggest_value)

    def test_get_index(self):
        expected_index = self.integer_list.get_index(2)
        self.assertEqual(1, expected_index)


if __name__ == "__main__":
    main()
