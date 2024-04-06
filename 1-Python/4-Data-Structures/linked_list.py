import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = ListNode(data)

        '''Scenario 1: Linked List is empty'''
        if self.head is None:
            self.head = new_node
            return

        '''Scenario 2: Linked List has nodes already'''
        cur = self.head

        while cur.next:
            cur = cur.next

        cur.next = new_node

    def prepend(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.start = self.cur = ListNode()
        min_val, max_val = 1, 10
        i = 1

        while self.cur and i <= max_val:
            new_node = ListNode(i)
            self.cur.next = new_node
            self.cur = self.cur.next
            i += 1

        self.start = self.start.next

    def test_linked_list_iteration(self):
        pt = self.start
        ans = []

        while pt:
            ans.append(pt.val)
            pt = pt.next

        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ans)
        self.assertEqual(None, pt)

        with self.assertRaises(AttributeError):
            next_pt = pt.next


if __name__ == '__main__':
    unittest.main()
