# python code for deletion at beginning using linked list.
from typing import Optional


class Node:
    def __init__(self, data: int, next: Optional['Node'] = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # display the list
    def print_list(self):
        p = self.head
        print("\n[", end="")
        while p:
            print(f" {p.data} ", end="")
            p = p.next
        print("]")

    # Insertion at the beginning
    def insert_at_begin(self, data: int):
        lk = Node(data)
        # point it to old first node
        lk.next = self.head
        # point first to new first node
        self.head = lk

    def delete_at_begin(self):
        self.head = self.head.next

    def delete_at_end(self):
        linkedlist = self.head
        while linkedlist.next.next is not None:
            linkedlist = linkedlist.next
        linkedlist.next = None

    # deletes node at position
    def deletenode(self, key):
        temp = self.head
        if temp is not None and temp.data == key:
            self.head = temp.next
            return
        # Find the key to be deleted
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next
        # If the key is not present
        if temp is None:
            return

            # Remove the node
        prev.next = temp.next


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_begin(12)
    linked_list.insert_at_begin(22)
    linked_list.insert_at_begin(30)
    linked_list.insert_at_begin(44)
    linked_list.insert_at_begin(50)
    # print list
    print("Original Linked List: ", end="")
    linked_list.print_list()
    linked_list.delete_at_begin()
    print("Linked List after deletion at beginning: ", end="")
    linked_list.print_list()
    linked_list.delete_at_end()
    print("Linked List after deletion at end: ", end="")
    linked_list.print_list()
    linked_list.deletenode(30)
    print("Linked List after deletion at position: ", end="")
    linked_list.print_list()
