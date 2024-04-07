import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None    # will always reflect the first node in linked list

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

    def delete(self, key):

        prev = None
        cur = self.head

        while cur:
            if cur.val == key:
                if prev:
                    '''When the element is present in middle to last position'''
                    prev.next = cur.next
                    # cur = None
                else:
                    '''When the element is present in first position'''
                    self.head = cur.next
                return
            prev = cur
            cur = cur.next

    def show_elements(self):
        elements = []
        cur = self.head

        while cur:
            elements.append(cur.val)
            cur = cur.next

        return elements


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_append_elements(self):

        min_val, max_val = 1, 10

        for i in range(min_val, max_val+1):
            self.linked_list.append(i)

        cur = self.linked_list.head

        j = 1

        while cur and j <= max_val:
            self.assertEqual(j, cur.val)
            cur = cur.next
            j += 1

        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], self.linked_list.show_elements())
        self.assertEqual(None, cur)

        with self.assertRaises(AttributeError):
            check = cur.next

    def test_prepend_elements(self):
        self.linked_list.prepend(0)
        self.linked_list.prepend(-1)
        self.linked_list.prepend(-2)

        min_val, max_val = -2, 0
        cur = self.linked_list.head
        j = min_val

        while cur and j <= max_val:
            self.assertEqual(j, cur.val)
            cur = cur.next
            j += 1

        self.assertEqual([-2, -1, 0], self.linked_list.show_elements())

    def test_delete_elements(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        self.linked_list.append(4)

        self.linked_list.delete(1)
        self.assertEqual([2, 3, 4], self.linked_list.show_elements())
        self.linked_list.delete(3)
        self.assertEqual([2, 4], self.linked_list.show_elements())
        self.linked_list.delete(4)
        self.assertEqual([2], self.linked_list.show_elements())
        self.linked_list.delete(2)
        self.assertEqual([], self.linked_list.show_elements())
        self.linked_list.delete(11)
        self.assertEqual([], self.linked_list.show_elements())


if __name__ == '__main__':
    unittest.main()
