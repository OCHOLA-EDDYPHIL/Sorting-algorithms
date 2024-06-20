class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:  # if the list is empty
            self.head = new_node
            new_node.next = self.head  # link it to itself(making it circular)
        else:
            temp = self.head
            while temp.next != self.head:  # traverse to the last node
                temp = temp.next
            temp.next = new_node  # set the next of the last node to the new node
            new_node.next = self.head  # link the new node back to the head

    def delete(self, key):
        if self.head is None:  # if the list is empty
            print("The list is empty.")
            return

        current = self.head  # start from the head of the list
        prev = None

        # Traverse the list to find the node to be deleted
        while 1:
            if current.data == key:
                break  # Node to be deleted found
            prev = current
            current = current.next
            if current == self.head:
                print("Node not found.")
                return

        # Case 1 -> The list has only 1 node
        if current == self.head and current.next == self.head:
            self.head = None
        else:
            # Case 2 -> The node to be deleted is the head node
            if current == self.head:
                # Find the last node to update its next pointer
                last = self.head
                while last.next != self.head:
                    last = last.next
                self.head = self.head.next  # update the head
                last.next = self.head  # Update last node's next to new head

            # Case 3 -> The node to be deleted is the last node
            elif current.next == self.head:
                prev.next = self.head  # link previous node to head

            # Case 4 -> The node to be deleted is neither first nor last
            else:
                prev.next = current.next  # Link previous node to next of current

        print(f"Node with data {key} deleted.")

    def display(self):
        if self.head is None:
            print("The list is empty.")
            return
        current = self.head
        while 1:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("END")


def main():
    list1 = LinkedList()

    while 1:
        node_data = input("Enter a data(i.e. number) for the node('stop' to finish): ").strip()
        if node_data.lower() == 'stop' or node_data == '':
            break
        if node_data:
            try:
                node_data = int(node_data)  # convert input into integer
                list1.append(node_data)  # only append if the input is not empty
            except ValueError:
                print("Invalid input. Please enter an integer")
    print("The circular linked list is: ")
    list1.display()

    while list1.head is not None:
        key = input("Enter a data of the node to delete(enter 'q' to quit): ").strip()
        if key.lower() == 'q' or key == '':
            break
        if key:
            try:
                key = int(key)  # convert input to integer
                list1.delete(key)
                print("Current list: ")
                list1.display()
            except ValueError:
                print("Invalid input. Please enter an integer")


if __name__ == "__main__":
    main()
