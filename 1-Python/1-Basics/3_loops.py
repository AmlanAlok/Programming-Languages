import unittest


class MyTestCase(unittest.TestCase):

    def test_while_loop(self):
        nums = []

        i = 0
        while i < 10:
            nums.append(i)
            i += 1

        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], nums)

    def test_for_loop(self):
        nums = []

        for i in range(10):
            nums.append(i)

        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], nums)
        nums.clear()

        for i in range(4, 9):
            nums.append(i)

        self.assertEqual([4, 5, 6, 7, 8], nums)
        nums.clear()

        for i in range(1, 10, 2):
            nums.append(i)

        self.assertEqual([1, 3, 5, 7, 9], nums)
        nums.clear()

        for i in range(10, 0, -1):
            nums.append(i)

        self.assertEqual([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], nums)
        nums.clear()

    def test_new_for_loop(self):

        nums = [1, 2, 3]
        a = []

        for i in nums:
            a.append(i)

        self.assertEqual([1, 2, 3], a)
        a.clear()

        fruits = ["apple", "banana", "cherry"]
        for fruit in fruits:
            a.append(fruit)

        self.assertEqual(["apple", "banana", "cherry"], a)

        stocks = {'AAPL': 187.31, 'MSFT': 124.06, 'FB': 183.50}
        for key, value in stocks.items():
            print(f"{key} : {value}")






if __name__ == '__main__':
    unittest.main()
