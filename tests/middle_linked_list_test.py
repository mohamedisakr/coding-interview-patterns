from unittest import TestCase, main

# Assuming your solution is in a file called solution.py
from fast_slow_pointers.middle_linked_list import find_middle, Node

# Assuming your LinkedList and Node classes are in a file called linkedlist.py
# from linkedlist import LinkedList, Node


class TestFindMiddleNode(TestCase):
    """test class for linked list middle node """

    def setUp(self):

        self.head1 = Node(1)
        self.head1.next = Node(2)
        self.head1.next.next = Node(3)
        self.head1.next.next.next = Node(4)
        self.head1.next.next.next.next = Node(5)

        # self.head2 = LinkedList()
        self.head2 = Node(10)
        self.head2.next = Node(20)
        self.head2.next.next = Node(30)

        # self.list3 = LinkedList()
        self.head3 = Node(100)

        # self.list4 = LinkedList()

    def test_find_middle_node(self):
        """ Test the expected outputs
        """
        self.assertEqual(find_middle(self.head1).value, 3)
        self.assertEqual(find_middle(self.head2).value, 20)
        self.assertEqual(find_middle(self.head3).value, 100)
        # self.assertIsNone(find_middle(self.list4))


if __name__ == '__main__':
    main()
