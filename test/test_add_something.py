import unittest
from ut_test.add_something import AddClass


class TestAddClass(unittest.TestCase):
    def test_add_one(self):
        t = AddClass()
        self.assertEqual(4, t.add_one(3))

    def test_add_ab(self):
        t = AddClass()
        self.assertEqual(7, t.add_ab(3, 4))


if __name__ == "__main__":
    unittest.main()
