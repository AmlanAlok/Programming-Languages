import unittest
from collections import deque

''' 
1. Pronounced "Deck" -> Double-Ended Queue
2. Thread-Safe
3. O(1) = append(), appendleft(), pop(), popleft()
4. IndexError: pop from an empty deque
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = deque()
        self.stack.append(1)
        self.stack.append(2)
        self.stack.append(3)

    '''Test Pop operation'''
    def test_01(self):
        self.assertEqual(1, self.stack[0])
        self.assertEqual(2, self.stack[1])
        self.assertEqual(3, self.stack[2])
        self.assertEqual(3, self.stack[-1])

    '''Test Stack Underflow'''
    def test_03(self):
        self.assertEqual(3, self.stack.pop())
        self.assertEqual(1, self.stack.popleft())
        self.assertEqual(2, self.stack.pop())

        with self.assertRaises(IndexError):
            self.stack.pop()

        with self.assertRaises(IndexError):
            last = self.stack[-1]


if __name__ == '__main__':
    unittest.main()
