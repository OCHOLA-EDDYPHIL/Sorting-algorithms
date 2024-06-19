class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def listprint(self):
        value = self.head
        print("Linked List: ")
        while value is not None:
            print(f"{value.data}", end="->")
            value = value.next
        print("end")

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return  # exits the method
        last = self.head  # start from the list
        while last.next:
            last = last.next
        last.next = new_node


list1 = Linkedlist()

while True:
    data = input(
        "Enter data (stop to end): "
    )
    if data.lower() == 'stop':
        break
    list1.insert(data)
print("The linked list is: ")
list1.listprint()
