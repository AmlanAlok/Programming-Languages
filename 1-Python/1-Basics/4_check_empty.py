import unittest


def is_empty(var):
    if var:
        return False
    else:
        return True


class MyTestCase(unittest.TestCase):

    def test_empty_none(self):
        self.assertEqual(is_empty(None), True)

    def test_empty_list(self):
        self.assertEqual(is_empty([1]), False)
        self.assertEqual(is_empty([]), True)

        self.assertEqual(len([1]) == 0, False)
        self.assertEqual(len([]) == 0, True)

        a = []
        self.assertEqual(a == [1], False)
        self.assertEqual(a == [], True)

    def test_empty_string(self):
        self.assertEqual(is_empty('Amlan'), False)
        self.assertEqual(is_empty(''), True)

    def test_empty_dict(self):
        self.assertEqual(is_empty({1: 'Amlan', 2: 'Alok'}), False)
        self.assertEqual(is_empty({}), True)

    def test_empty_tuple(self):
        self.assertEqual(is_empty((1, 2, 3)), False)
        self.assertEqual(is_empty(()), True)

    def test_empty_set(self):
        self.assertEqual(is_empty({1, 2, 3}), False)
        empty_set = set()
        self.assertEqual(is_empty(empty_set), True)


if __name__ == '__main__':
    unittest.main()
