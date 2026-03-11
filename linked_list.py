# Singly linked lists can add a new element at the beginning (head) of the list
# and remove an element from the head of the list

class Empty(Exception):
    pass
class Node:
    '''The Node class represents an element of a singly linked list

    The node contains two references: a reference to the value and
    a reference to the next node.
    '''
    def __init__(self, element, next=None):
        self.element = element   # A reference to the value
        self.next = next         # A reference to the next node

class SinglyLinkedList:
    'A basic singly linked list implementation'

    def __init__(self):
        self.head = None

    def add_first(self, element):
        'Add a new element at the head of the linked list'
        # 1. Create a node
        # 2. Set the node's next pointer to current head
        new_node = Node(element, self.head)
        # 3. Update the head pointer
        self.head = new_node

    def remove_first(self):
        'Remove and return the first element from the head of the list'

        # First check if we have any elements in the list. If not, raise
        # the Empty exception (defined earlier for stacks and queues)
        if self.head is None:
            raise Empty('The list is empty')

        # Save a reference to the current node at the head of the list
        node = self.head

        # Update the head pointer to point to the next element. If there
        # is no next element, it will be set to None
        self.head = self.head.next

        # Since node is no longer in the list, we can set its _next
        # reference to None to help the Python garbage collector
        node.next = None

        # Finally, return the node's value
        return node.element


class SinglyLinkedList:
    'A basic singly linked list implementation with tail and size'

    def __init__(self):
        self.head = None
        self.tail = None  # NEW: We have added this instance variable
        self.size = 0     # NEW: We have added this instance variable
    
    def add_first(self, element):
        'Add a new element at the head of the linked list'
        # 1. Create a node
        # 2. Set the node's next pointer to current head
        new_node = Node(element, self.head)
        # 3. Update the head pointer
        self.head = new_node

        # If the list was previously empty, we also need to update the
        # tail to point to the newly added node. That is needed because
        # the list only contains one node, and both head and tail should
        # point to that node.
        if self.size == 0:
            self.tail = new_node

        self.size += 1
    
    def remove_first(self):
        'Remove and return the first element from the head of the list'

        # First check if we have any elements in the list. If not, raise
        # the Empty exception (defined earlier for stacks and queues)
        if self.size == 0:
            raise Empty('The list is empty')

        # Save a reference to the current node at the head of the list
        node = self.head

        # Update the head pointer to point to the next element. If there
        # is no next element, it will be set to None
        self.head = self.head.next

        # Since node is no longer in the list, we can set its _next
        # reference to None to help the Python garbage collector
        node.next = None

        self.size -= 1

        # If we removed the last element from the list, we also need to
        # set the tail pointer to None, since there are no more nodes
        if self.size == 0:
            self.tail = None
        
        # Finally, return the node's value
        return node.element

    # NEW: Keeping a reference to the tail allows us to implement the
    # following method in constant time
    def add_last(self, element):
        'Add a new element at the tail of the linked list'
        # 1. Create a new node
        new_node = Node(element, None)

        # 2. Set the previous node's next to the new node

        if self.size == 0:
            self.head = new_node
        else:    
            self.tail.next = new_node        
            # 3. Update the tail pointer

        self.tail = new_node
        self.size += 1


# Implementing a stack using a singly linked lists:
class LinkedStack:
    def __init__(self):
        self._data = SinglyLinkedList()

    def push(self, el):
        self._data.add_first(el)

    def pop(self):
        return self._data.remove_first()
    
stack = LinkedStack()
stack.push(42)
stack.push("alpha")
stack.push("python")

print(stack.pop()) # expecting: python
print(stack.pop()) # expecting: alpha
print(stack.pop()) # expecting: 42


# Implementing a queue with a singly linked list:
class LinkedQueue:
    def __init__(self):
        self._data = SinglyLinkedList()
    
    def enque(self, el):
        self._data.add_last(el)

    def deque(self):
        return self._data.remove_first()

queue = LinkedQueue()
queue.enque(42)
queue.enque("alpha")
queue.enque("python")

print(queue.deque()) # expecting: 42
print(queue.deque()) # expecting: alpha
print(queue.deque()) # expecting: python


# We extend the node class developed for the singly linked list. The modification consists of adding the "prev" link:
class Node:
    def __init__(self, element, prev, next):
        self.element = element
        self.next = next
        self.prev = prev
# ↓ ↓ ↓ becomes
class DoublyLinkedList:
    def __init__(self):
        self.header = Node(None, None, None)
        self.trailer = Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    # Auxilialy methods
    def __len__(self):
        pass

    def is_empty(self):
        pass

    def _insert_between(self, e, predecessor, successor):
        'Insert element e between the two nodes'
        pass
    
    def _delete_node(self, node):
        'Delete the node "node"'
        pass

# To insert a node:
def _insert_between(self, e, predecessor, successor):
    new_node = Node(e, predecessor, successor)
    predecessor.next = new_node
    successor.prev = new_node
    self.size += 1
    return new_node

# Removing a node:
def _delete_node(self, node):
    el = node.element
    
    predecessor = node.prev
    successor = node.next

    successor.prev = node.prev
    predecessor.next = node.next
    self.size -= 1
 
    return el
