# Python code for doubly linked list

class Node:
    def __init__(self, data=None, key=None):
        self.data = data
        self.key = key
        self.next = None
        self.prev = None


# this link always points to the first link
head = None

# this link always point to the last link
last = None

current = None


# is list empty

def is_empty():
    return head is None


# display the doubly linked list

def print_list():
    pointer = head
    while pointer is not None:
        print(f"{pointer.key}, {pointer.data}")
        pointer = pointer.next


# insert link at the first location

def insert_first(key, data):
    global head, last

    # Create a link

    link = Node(data, key)
    if is_empty():

        # make it the last link
        last = link
    else:
        # update first prev link
        head.prev = link

    # point it to old first link
    link.next = head

    # point first to new first link
    head = link


def insert_last(key, data):
    global head, last
    link = Node(data, key)
    if is_empty():
        last = link
    else:
        last.next = link
        link.prev = last

    last = link


insert_first(1, 10)
insert_first(2, 20)
insert_first(3, 30)
insert_first(4, 40)
insert_first(5, 50)
insert_first(6, 60)
insert_last(7, 70)
insert_last(8, 80)

print("Doubly Linked List: ", end="")
print_list()
