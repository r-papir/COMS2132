'''Building & Traversing a Binary Tree'''

class ArrayQueue(object):
    '''A queue backed with a built-in Python list'''

    def __init__(self):
        # Creates an empty ArrayQueue instance      
        self.queue = []

    def enqueue(self, element):
    # Enqueue element at the back of the queue
        self.queue.append(element)

    def dequeue(self):
        # Dequeue the element from the front of the queue
        # Raise an exception if the queue is empty
        if len(self.queue) == 0:
            raise IndexError("Queue is empty!")
        return self.queue.pop(0)
        
    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if len(self.queue) == 0:
            raise IndexError("Queue is empty!")
        else:
            return self.queue[0].value
        
    def __len__(self):
    # Return the length of the queue
        return len(self.queue)

class Node(object):
    def __init__(self, value):  # initializer always comes first!
        self.value = value      # assigns whatever is passed into the class variable to 'value'
        self.left = None        # sets up our left children
        self.right = None        # sets up our right children

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)  # this is an ARGUMENT that assigns the class variable 'root' to a node of the tree

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "breadth-first":
            return self.breadth_first_print(tree.root)
        else:
            print("Traversal Type " + str(traversal_type) + " is not supported.")

    def preorder_print(self, starting_node, traversal_string):      # the PARAMETERS are 'self', 'starting_node', and 'traversal_string'
        # this function takes 'self' because it's a member of its own class --> recursion!
        '''Root → Left → Right'''
        if starting_node:
            traversal_string += (str(starting_node.value) + "→")    # this creates a counter that stores all the nodes we find in a string, separating them with a dash
            traversal_string = self.preorder_print(starting_node.left, traversal_string)    # here the function recursively calls itself with 'self'
            traversal_string = self.preorder_print(starting_node.right, traversal_string)
        return traversal_string
    
    def inorder_print(self, starting_node, traversal_string):
        '''LEFT → ROOT → RIGHT'''
        if starting_node:
            traversal_string = self.inorder_print(starting_node.left, traversal_string)
            traversal_string += (str(starting_node.value) + "→")
            traversal_string = self.inorder_print(starting_node.right, traversal_string)
        return traversal_string
    
    def postorder_print(self, starting_node, traversal_string):
        '''LEFT → RIGHT → ROOT'''
        if starting_node:
            traversal_string = self.postorder_print(starting_node.left, traversal_string)
            traversal_string = self.postorder_print(starting_node.right, traversal_string)
            traversal_string += (str(starting_node.value) + "→")    # wherever you place the counter denotes which order the root will be traversed
        return traversal_string
    
    def breadth_first_print(self, starting_node):
        if starting_node is None:
            return
        
        queue = ArrayQueue()
        queue.enqueue(starting_node)
        traversal_string = " "

        while len(queue) > 0:
            traversal_string += str(queue.peek()) + "→"     # parentheses must not include → because the peek() operation is dealing with the data itself, not just the string!
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal_string


tree = BinaryTree(1)  # sets the initial value of the tree to 1, which becomes the root
tree.root.left = Node(2)  # sets the initial value of the tree to 1, which becomes the root
tree.root.right = Node(3)   # sets the left node (child) of the root to 2
tree.root.left.left = Node(4) # sets the right node (child) of the root to 3
tree.root.left.right = Node(5)  # and so on...
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

'''Our tree looks like this:'''
#          1
#       /     \
#      2       3
#    /  \     /  \
#   4    5   6    7
'''Try printing the tree using different traversal methods!'''

def user_select():

    while True:
        print(" ")
        print("TRAVERSAL METHODS:")
        print("[A] Preorder")
        print("[B] Inorder")
        print("[C] Postorder")
        print("[D] Breadth-First")
        print("[E] Exit ")
        print(" ")

        selection = input("Please enter a letter from the options above: ")

        if selection == "A" or selection == "a":
            print(" ")
            print(tree.print_tree("preorder"))
            print(" ")
        elif selection == "B" or selection == "b":
            print(" ")
            print(tree.print_tree("inorder"))
            print(" ")
        elif selection == "C" or selection == "c":
            print(" ")
            print(tree.print_tree("postorder"))
            print(" ")
        elif selection == "D" or selection == "d":
            print(" ")
            print(tree.print_tree("breadth-first"))
            print(" ")
        elif selection == "E" or selection == "e":
            print("Goodbye.")
            break
        else:
            print("Invalid selection; please try again.")

user_select()