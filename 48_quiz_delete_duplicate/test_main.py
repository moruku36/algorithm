import unittest

from main import (
    delete_duplicate_v1,
    delete_duplicate_v2,
    delete_duplicate_v3,
    delete_duplicate_v4,
)

class TestDeleteDuplicate(unittest.TestCase):
    def setUp(self):
        self.funcs = [
            delete_duplicate_v1,
            delete_duplicate_v2,
            delete_duplicate_v3,
            delete_duplicate_v4,
        ]

    def test_empty_list(self):
        for func in self.funcs:
            with self.subTest(func=func.__name__):
                lst = []
                lst_id = id(lst)
                result = func(lst)
                self.assertIsNone(result)
                self.assertEqual(lst, [])
                self.assertEqual(id(lst), lst_id)

    def test_singleton_list(self):
        for func in self.funcs:
            with self.subTest(func=func.__name__):
                lst = [42]
                lst_id = id(lst)
                result = func(lst)
                self.assertIsNone(result)
                self.assertEqual(lst, [42])
                self.assertEqual(id(lst), lst_id)

    def test_sorted_duplicate_list(self):
        for func in self.funcs:
            with self.subTest(func=func.__name__):
                lst = [1, 3, 3, 5, 5, 7, 7, 7, 10, 12, 12, 15]
                lst_id = id(lst)
                result = func(lst)
                self.assertIsNone(result)
                self.assertEqual(lst, [1, 3, 5, 7, 10, 12, 15])
                self.assertEqual(id(lst), lst_id)

if __name__ == '__main__':
    unittest.main()
