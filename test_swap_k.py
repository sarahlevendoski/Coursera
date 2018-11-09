import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_swap_k_where_list_is_empty(self):
        ''' Test swap_k when the list is empty and k == 0'''

        actual_list = []
        expected = []
        a1.swap_k(actual_list, 0)
        self.assertEqual(expected, actual_list)

    def test_swap_k_where_list_has_1_item(self):
        ''' Test swap_k when the list has 1 item k == 0'''

        actual_list = [1]
        expected = [1]
        a1.swap_k(actual_list, 0)
        self.assertEqual(expected, actual_list)

    def test_swap_k_where_list_has_3_items(self):
        ''' Test swap_k when the list has 3 items and k == 1'''

        actual_list = [1, 2, 3]
        expected = [3, 2, 1]
        a1.swap_k(actual_list, 1)
        self.assertEqual(expected, actual_list)

    def test_swap_k_where_list_has_4_items(self):
        ''' Test swap_k when the list has 4 items and k == 2'''

        actual_list = [1, 2, 3, 4]
        expected = [3, 4, 1, 2]
        a1.swap_k(actual_list, 2)
        self.assertEqual(expected, actual_list)

    def test_swap_k_where_list_has_5_items(self):
        ''' Test swap_k when the list has 5 items and k == 1'''

        actual_list = [1, 2, 3, 4, 5]
        expected = [5, 2, 3, 4, 1]
        a1.swap_k(actual_list, 1)
        self.assertEqual(expected, actual_list)


if __name__ == '__main__':
    unittest.main(exit=False)