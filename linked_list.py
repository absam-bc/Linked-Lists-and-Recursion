class Node:
    """
    A Node stores integer data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that performs operations using recursion.
    """

    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def recursive_sum(self):
        def calculate_sum(node):
            # Base case: an empty position contributes zero.
            if node is None:
                return 0

            # Recursive case: add this node and the remaining nodes.
            return node.data + calculate_sum(node.next)

        return calculate_sum(self.head)

    def recursive_reverse(self):
        def reverse_nodes(previous, current):
            # Base case: current is None, so previous is the new head.
            if current is None:
                return previous

            # Save the next node before changing the pointer.
            next_node = current.next

            # Point the current node backwards.
            current.next = previous

            # Continue reversing the remaining nodes.
            return reverse_nodes(current, next_node)

        self.head = reverse_nodes(None, self.head)

    def recursive_search(self, target):
        def search_node(node):
            # Base case: target was not found.
            if node is None:
                return False

            # Base case: target was found.
            if node.data == target:
                return True

            # Recursive case: search the next node.
            return search_node(node.next)

        return search_node(self.head)

    def display(self):
        values = []
        current = self.head

        while current is not None:
            values.append(str(current.data))
            current = current.next

        print(" -> ".join(values) + " -> None")
