class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class Linkedlist:
    def __init__(self):
        self.last = None
        self.head = None

    def listprint(self):
        value = self.head
        while value is not None:
            print(f"{value.data}", end="->")
            value = value.next
        print("end")

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return  # exits the method
        else:
            last = self.head  # start from the list
            while last.next:
                last = last.next
            last.next = new_node

    # Bubble sort
    def sort(self):
        if self.head is None or self.head.next is None:
            return  # List is empty or has only one node

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                next_node = current.next
                if current.data > current.next.data:
                    # Swap the nodes not just the data
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next
            # end = current # move the end marker to the sorted section

    def merge(self, other_list):
        # Create a new instance to hold the merged elements
        merged_list = Linkedlist()
        if not other_list.head:
            return  # if the other list is empty, nothing to merge

        def append(node):
            while node:
                merged_list.insert(node.data)
                node = node.next

        append(self.head)  # adds nodes from self
        append(other_list.head)  # adds nodes from other list
        return merged_list

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return  # exits the method
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_in_middle(self, data):
        new_node = Node(data)
        if not self.head or not self.head.next:
            self.insert_at_beginning(data)
            return

        # two pointer to traverse the system slow(1x speed), fast(2x speed)
        slow = self.head
        fast = self.head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Insert new node after slow
        new_node.next = slow.next
        new_node.prev = slow
        if slow.next:
            slow.next.prev = new_node
        slow.next = new_node

    def find_middle(self):
        if not self.head:
            return None

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:  # if fast reaches the end, nodes = odd and slow is the middle
            return slow
        else:  # if fast = none, nodes = even and prev slow, slow are the middle
            return slow.prev, slow


def main():
    list1 = Linkedlist()
    list2 = Linkedlist()

    while True:
        list1.data = input("Enter data for list one(stop to end): ").strip()
        if list1.data.lower() == 'stop' or list1.data == '':
            print("Now we populate the second list........")
            break
        data = int(list1.data)
        list1.insert(data)
    while True:
        list2.data = input("Enter data for list two(stop to end): ").strip()
        if list2.data.lower() == 'stop' or list2.data == '':
            break
        data = int(list2.data)
        list2.insert(data)

    print("list 1: ")
    list1.listprint()

    print("list 2: ")
    list2.listprint()

    merged_list = list1.merge(list2)
    print("merged list: ")
    merged_list.listprint()

    list1.sort()
    print("sorted list 1: ")
    list1.listprint()

    list2.sort()
    print("sorted list 2: ")
    list2.listprint()

    merged_list.sort()
    print("sorted merged list: ")
    merged_list.listprint()

    while True:
        merged_list.data = input("Enter data at the beginning of the merged list(stop to end): ").strip()
        if merged_list.data.lower() == 'stop' or merged_list.data == '':
            print("Now we append in the middle.......")
            break
        data = int(merged_list.data)
        merged_list.insert_at_beginning(data)
        merged_list.listprint()

    data = int(input("Enter data to be append in the middle of the list: ").strip())
    merged_list.insert_in_middle(data)
    merged_list.listprint()

    middle = merged_list.find_middle()
    if isinstance(middle, tuple):
        print(f"The middle nodes of the merged list are {middle[0].data} and {middle[1].data}")
    else:
        print(f"The middle nodes of the merged list are {middle.data}")


if __name__ == "__main__":
    main()
