import unittest
import search


class Test(unittest.TestCase):
    def test_binary_search(self):

        test_list = [10, 20, 30, 40, 50, 60, 70]

        test_result = search.binary_search(test_list,20)
        self.assertEqual(test_result,1)

        test_result = search.binary_search(test_list, 70)
        self.assertEqual(test_result, 6)

        test_result = search.binary_search(test_list, 100)
        self.assertEqual(test_result, None)