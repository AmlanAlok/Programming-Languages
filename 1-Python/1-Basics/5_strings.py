import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_strings_comparison(self):
        """
        In Python, the comparison operators (<, >, <=, >=) work with strings in this lexicographic order, which is
        similar to how words are sorted in a dictionary.
        """
        self.assertEqual('marya' > 'mary', True)
        self.assertEqual('abc' > 'acb', False)


if __name__ == '__main__':
    unittest.main()
