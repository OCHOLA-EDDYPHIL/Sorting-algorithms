class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    # Print the Linked List
    def list_print(self):
        value = self.head
        while value is not None:
            print(f'{value.data}', end=' ')
            value = value.next

    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous


list1 = LinkedList()
list1.head = Node("1")
e2 = Node("2")
e3 = Node("3")

list1.head.next = e2
e2.next = e3

list1.list_print()
list1.reverse()
print("After reversing: ")
list1.list_print()