# Define a class to represent a node in the linked list
class Node:
    # Constructor to initialize the node object
    def __init__(self, data=None):
        # Assign data to the node
        self.data = data
        # Initialize next as null
        self.next = None


# Define a class to represent the singly linked list (SLL)
class SLL:
    # Constructor to initialize the singly linked list
    def __init__(self):
        # Initialize head as null (indicating the list is empty)
        self.head = None

    # Method to print the linked list
    def listprint(self):
        # Initialize the print pointer to the head of the list
        print_value = self.head
        print("Linked List: ")
        # Traverse the list until the end
        while print_value is not None:
            # Print the data at the current node
            print(print_value.data)
            # Move to the next node
            print_value = print_value.next

    # Method to add a new node at the beginning of the list
    def add_at_beginning(self, new_data):
        # Create a new node with the given data
        new_node = Node(new_data)
        # Point the next of the new node to the current head
        new_node.next = self.head
        # Update the head to point to the new node
        self.head = new_node


# Create an instance of SLL (Singly Linked List)
linkedList1 = SLL()
# Create the first node and set it as the head of the list
linkedList1.head = Node("731")
# Create two more nodes
e2 = Node("672")
e3 = Node("63")
# Link the first node to the second node
linkedList1.head.next = e2
# Link the second node to the third node
e2.next = e3

# Add a new node at the beginning of the list
linkedList1.add_at_beginning("122")
linkedList1.add_at_beginning("46")
linkedList1.add_at_beginning("67")
linkedList1.add_at_beginning("90")
# Print the linked list
linkedList1.listprint()
