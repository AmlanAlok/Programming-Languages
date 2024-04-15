import unittest
import sys


class MyTestCase(unittest.TestCase):

    def test_read_input(self):
        # x = input('Enter: ')
        x = 'polo'
        self.assertEqual(x, 'polo')

    def test_math_func(self):
        self.assertEqual(4 + 2, 6)
        self.assertEqual(4 - 2, 2)
        self.assertEqual(4 * 2, 8)
        self.assertEqual(4 / 2, 2)

        self.assertEqual(5 // 2, 2)  # floor operation
        self.assertEqual(-5 // 2, -3)  # floor operation
        self.assertEqual(5 % 2, 1)  # modulo operation
        self.assertEqual(4 % 2, 0)  # modulo operation

        self.assertEqual(max(6, 2), 6)
        self.assertEqual(min(6, 2), 2)
        self.assertEqual(max([1, 2, 3]), 3)
        self.assertEqual(min([1, 2, 3]), 1)

    def test_max_num(self):
        max_num = sys.maxsize
        self.assertEqual(9223372036854775807, max_num)


if __name__ == '__main__':
    unittest.main()
