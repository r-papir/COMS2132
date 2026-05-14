# Abstract Data Types: Binary Trees
In computer science, a tree is an abstract model of a hierarchical structure. A **binary tree** is an abstract data structure in which each node has no more than two children, which are referred to as the "left child" and "right child". Unlike in *linked lists*, binary trees have pointers that link each node to its children. Trees often offer faster than linear algorithms (for example, *binary search*). When reading a binary tree, the **left child** always precedes the **right child**, and they can be written as an *ordered pair*.

<img width="501" height="408" alt="tree" src="https://github.com/user-attachments/assets/466e2e46-38e9-430d-82c0-eeba66fbe2de" /> 

**Terminology:**
|   |   |   |
| :---: | :---: | :---: |
| child | parent | root |
| leaves | ancestor | descendant |
| subtree | depth | height | 


+ Tree *T* (above) is a set of nodes storing elements that have a **parent-child** relationship.
+ The first (or 'highest') node in a tree is called the **root**. In the image above, the root is *A*.
+ Children of the same parent are **siblings**, and all *internal* nodes have at least one child.
+ Nodes that have no children are called **leaves** (also *external*).
+ A **subtree** at *C* is the tree of all the descendants of *C* in the tree (including *C* itself).

+ The **depth** of a node describes the number of ancestors from that node.
+ The **height** of a tree (or subtree) describes the *maximum depth* of any node.
+ If the order among the children is important, we call it an *ordered* tree.


## Video Lession

[![Binary Search](https://img.youtube.com/vi/9nmrkG6QtpQ/0.jpg)](https://www.youtube.com/watch?v=9nmrkG6QtpQ)
[![Binary Trees](https://img.youtube.com/vi/EPwWrs8OtfI/0.jpg)](https://www.youtube.com/watch?v=EPwWrs8OtfI)

### §1: Building a Binary Tree
```python
class Node(object):
    def __init__(self, value):    # init constructer always comes first!
        self.value = value    # assigns whatever is passed into the class variable to 'value'
        self.left = None    # sets up our left children
        self.righ = None    # sets up our right children

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)    # assigns the class variable 'root' to a node of the tree

# ________________________________________

tree = BinaryTree(1)    # sets the initial value of the tree to 1, which becomes the root
tree.root.left = Node(2)    # sets the left node (child) of the root to 2
tree.root.right = Node(3)    # sets the right node (child) of the root to 3
tree.root.left.left = Node(4)    # and so on...
tree.root.left.right = Node(5)
tree.root.right.light = Node(6)
tree.root.right.right = Node(7)
```
**Our tree now looks like this:**
```python
#          1
#       /     \
#      2       3
#    /  \     /  \
#   4    5   6    7
```

### §2: Traversing a Binary Tree
How do we use and move through trees? In this section, we will discuss selected tree traversal algorithms, i.e., algorithms that systematically access (or visit) all positions in a tree exactly one time. The algorithm will perform some action for each visited position as part of the visit. These actions could involve simple or complex computations, depending on the application.

There are several systematic ways of visiting all positions of a tree:
+ **Preorder:** the position is visited first, followed by recursive visits to all its children (*DFS order*)
+ **Postorder:** the children of a node are visited before the node itself is visited (*DFS order*)
+ **Inorder:** a subset of children is visited first, then the position itself, and then the rest of the children. Inorder traversal is mostly applicable to binary trees. (*DFS order*)
+ **Breadth-First:** The positions are visited according to their depth (root first, then all nodes at depth 1, then all nodes at depth 2, and so on)


**<ins>Preorder Traversal</ins> (DFS)**

**<ins>Postorder Traversal</ins> (DFS)**

**<ins>Inorder Traversal</ins> (DFS)**
We can store this [word list](https://github.com/r-papir/my_games/blob/main/wordle.txt) in a binary tree structure like this:

```python
# Write the _insert_below and insert method and insert them in the AbstractBinaryTree class

def _insert_below(self, p, e):
    if e < p.element():
        if self.left(p):
            self._insert_below(self.left(p), e)
        else:
            self._add_left(p, e)
    else:
        if self.right(p):
            self._insert_below(self.right(p), e)
        else:
            self._add_right(p, e)

def insert(self, e):
    if self.is_empty():
        self._add_root(e)
    else:
        self._insert_below(tree.root(), e)

AbstractBinaryTree._insert_below = _insert_below
AbstractBinaryTree.insert = insert
```



**<ins>Breadth-First Traversal</ins> (BFS)**


### Linked Trees

<img width="935" height="555" alt="tree-linked" src="https://github.com/user-attachments/assets/b35b47b6-b8de-4385-9411-5a0362233bca" />

**Maniuplating and Updating a Tree Structure:** **The following operations have a runtime of O(1).*
|  Operation | How it works  |
| :---: | :--- |
| add_root(e) | create a root for an empty tree |
| add_left(p,e) | link the node as left child of p |
| add_right(p,e) | link the node as right child of p | 
| replace(p,e) | replace the element stored at p with e | 
| delete(p) |  remove the node at p, replacing it with its child (if any) and return the element (reports error if there are multiple children) | 
| attach(p,t1,t2) | attach the internal structures of t1 and t2 as left and right subtrees of leaf p | 

***Can you find these operations in the program below?***

```python
class LinkedBinaryTree(AbstractBinaryTree):
    class _Node:
        def __init__(self, element, parent=None, left=None, right=None):
          self._element = element
          self._parent = parent            
          self._left = left
          self._right = right
                
    class Position(AbstractPosition):
        def __init__(self, container, node):
            self._container = container # This is a reference to the tree containing the node
            self._node = node
        
        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
            
    def _make_position(self, node):
        "Converts a node to the node's position in the tree"
        if node is None:
            return None
        else:
            return self.Position(self, node)

    def _validate(self, p): # retrieve the node object in position p 
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def __init__(self):
        'Create an empty linked binary tree'
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        'Return the parent of the node at position p or none if p is root'
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    # Constant time operation
    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    # Constant-time operation
    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    # Constant-time operation
    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old
                
    def _delete(self, p):
        node = self._validate(p)

        # We cannot easily delete a node that has two children. If the
        # node has only one child, the child could be plugged into the
        # tree instead of the parent being removed. But there is no easy
        # way to plug the other child.
        if self.num_children(p) == 2:
            raise ValueError('Position has two children')
            
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
            
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child

        self._size -= 1
        node._parent = node
        return node._element
        
    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old
  
    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
            
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
    
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0
```

<!--
The len method takes $O(1)$
Method is_empty (inherited) calls len() and is thus $O(1)$
Methods root, left, right, parent, and num_children are all $O(1)$
Methods siblings and children (inherited from AbstractBinaryTree) use a constant number of accessors and are $O(1)$
is_root and is_leaf are both $O(1)$
depth is $O(d_p + 1)$
height is $O(n)$
The various update methods are all -->

### Accessor Methods:
```python

p.element(): # returns the element stored at position p

T.root(): # returns the position of the root of tree T, or None if T is empty

T.is_root(p): # returns True if position p is the root of Tree T

T.parent(p): # returns the position of the parent of position p, or None if p is the root of T

T.num_children(p): # returns the number of children of position p

T.children(p): # generates an iteration of the children of position p

T.is_leaf(p): # returns True if position p does not have any children

len(T): # returns the number of positions (and hence elements) that are contained in tree T

T.is_empty(): # returns True if tree T does not contain any positions

T.positions(): # generates an iteration of all positions of tree T

iter(T): # generates an iterations of all elements stored within tree T

```



<!-- [![Alt text for image](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID) -->
