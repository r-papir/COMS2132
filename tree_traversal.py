'''Building & Traversing a Binary Tree'''

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
        else:
            print("Traversal Type " + str(traversal_type) + " is not supported.")

    def preorder_print(self, starting_node, traversal_string):      # the PARAMETERS are 'self', 'starting_node', and 'traversal_string'
        # this function takes 'self' because it's a member of its own class --> recursion!
        '''Root --> Left --> Right'''
        if starting_node:
            traversal_string += (str(starting_node.value) + "→")    # this creates a counter that stores all the nodes we find in a string, separating them with a dash
            traversal_string = self.preorder_print(starting_node.left, traversal_string)    # here the function recursively calls itself with 'self'
            traversal_string = self.preorder_print(starting_node.right, traversal_string)
        return traversal_string
    
    def postorder_print(self, starting_node, traversal_string):
        

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
'''Try printing the tree using different traversal methods.'''

print(tree.print_tree("preorder")) # here we specify the traversal type
