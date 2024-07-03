class Node:
    def __init__(self, key, data):
        self.data = data
        self.next = None
        self.key = key


head = None
current = None


def is_empty():
    return head is None


def insert(key, data):
    global head
    new_node = Node(key, data)
    if is_empty():
        head = new_node
        head.next = head
    else:
        # point it to old first node
        new_node.next = head
        head = new_node


def print_list():
    global head
    pointer = head
    if head is not None:
        while pointer.next is not pointer:
            print("({},{})".format(pointer.key, pointer.data), end=" ")
            pointer = pointer.next


insert(1, 100)
insert(2, 200)
insert(3, 300)
insert(4, 400)

print("Circular Linked list: ")
print_list()
