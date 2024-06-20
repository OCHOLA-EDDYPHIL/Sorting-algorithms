class Node:
    def __init__(self, data=None, key=None):
        self.data = data
        self.key = key
        self.next = None
        self.prev = None


head = None

last = None

current = None


def isEmpty():
    return head is None


def printList():
    pointer = head
    while pointer is not None:
        print(f"({pointer.key},{pointer.data})", end=" ")
        pointer = pointer.next


def insertFirst(key, data):
    # create a link
    global head, last
    link = Node(data, key)

    if isEmpty():
        # make it the last link
        last = link
    else:
        # update first prev link
        head.prev = link
    # point it to old first link
    link.next = head
    head = link


# delete first item
def deleteFirst():
    # save reference to first link
    global head, last
    tempLink = head

    # if only one link
    if head.next is None:
        last = None
    else:
        head.next.prev = None
    head = head.next

    # return the deleted link
    return tempLink


def deleteLast():
    global head, last
    tempLink = head
    if tempLink.next is None:
        last = None
    else:
        last.prev.next = None
    last = last.prev
    return tempLink


def delete(key):
    global head, last, current
    current = head
    while current and current.key is not key:
        current = current.next
    if current is None:
        return None
    if current is head:
        head = head.next
    else:
        current.prev.next = current.next
    if current is last:
        last = current.prev
    else:
        current.next.prev = current.prev
    return current


def insert_after(key, new_key, data):
    global head, last, current
    current = head
    while current and current.key is not key:
        current = current.next
    if current is None:
        return 0
    new_link = Node(new_key, data)
    if current is last:
        new_link.next = None
        last = new_link
    else:
        new_link.next = current.next
        current.next.prev = new_link
    new_link.prev = current
    current.next = new_link
    return True


def display_backwards():
    global last
    pointer = last
    while pointer:
        print("({}, {})".format(pointer.key, pointer.data), end=" ")
        pointer = pointer.prev


insertFirst(1, 10)
insertFirst(2, 20)
insertFirst(3, 30)
insertFirst(4, 40)
insertFirst(5, 50)
insertFirst(6, 60)
insertFirst(7, 70)
insertFirst(8, 80)
print("Doubly Linked List: ")
printList()
print("\nList after deleting first record: ")
deleteFirst()
printList()
print("\nList after deleting last record: ")
deleteLast()
printList()
print("\nList after deleting specific record: ")
delete(4)
printList()
print("\n List after inserting key(4): ")
insert_after(6, 18, 55)
printList()
print("\n List displayed backwards: ")
display_backwards()
