#Ex 3
#linked lists- removing a node at a given location

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Function to add a node at the end of the list (for testing)
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Function to print the linked list (for testing)
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

    # Function to delete a node at a given location
    def deleteAtLocation(self, location):
        if not self.head: # If the list is empty
            print("List is empty.")
            return

        # If the location is 0, delete the head node
        if location == 0:
            self.head = self.head.next
            return

        # Traverse to the node before the one to be deleted
        current = self.head
        for _ in range(location - 1):
            if not current.next: # If the location is out of range
                print("Location out of range.")
                return
            current = current.next

        # If there is no node at the given location, return
        if not current.next:
            print("Location out of range.")
            return

        # Delete the node by adjusting the 'next' pointer
        current.next = current.next.next

# Testing the implementation
ll = LinkedList()
ll.append(12)
ll.append(56)
ll.append(76)
ll.append(11)
ll.append(0)

print("Original List:")
ll.print_list()

# Deleting the head (location = 0)
ll.deleteAtLocation(0)
print("\nAfter deleting node at location 0:")
ll.print_list()

# Deleting the node at location 3
ll.deleteAtLocation(3)
print("\nAfter deleting node at location 3:")
ll.print_list()
