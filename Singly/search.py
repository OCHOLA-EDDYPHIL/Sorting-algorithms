class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def list_print(self):
        value = self.head
        while value is not None:
            print(f'{value.data}', end=' ')
            value = value.next

    def search(self, val):
        count = 0

        # Initialize current to head
        current = self.head

        # Loop until current is not equal to none
        while current is not None:
            if current.data == val:
                print("Element is found")
                count += 1
            current = current.next
        if count == 0:
            print("Element is not found")


list1 = LinkedList()
list1.head = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
list1.head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

list1.list_print()
target = 40
print (f"Target is {target}")
list1.search(target)
