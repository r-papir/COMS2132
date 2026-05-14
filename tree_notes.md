# Abstract Data Types: Binary Trees
In computer science, a tree is an abstract model of a hierarchical structure. A **binary tree** is an abstract data structure in which each node has no more than two children, which are referred to as the "left child" and "right child". Unlike in *linked lists*, binary trees have pointers that link each node to its children. Trees often offer faster than linear algorithms (for example, *binary search*).

<img width="501" height="408" alt="tree" src="https://github.com/user-attachments/assets/466e2e46-38e9-430d-82c0-eeba66fbe2de" />

+ Tree *T* (above) is a set of nodes storing elements that have a parent-child relationship.
+ The first (or 'highest') node in a tree is called the **root**. In the image above, `root = A`.
+ Children of the same parent are **siblings**, and all *internal* nodes have at least one child.
+ Nodes that have no children are called **leaves** (also *external*).
+ A **subtree** at *C* is the tree of all the descendants of *C* in the tree (including *C* itself)

**Important Terminology:**
| :---: | :---: | :---: |
| child | parent | root |
| leaves | ancestor | descendant |
| leaves | ancestor | subtree |




**§1:** Video Lession

[![Binary Search](https://img.youtube.com/vi/9nmrkG6QtpQ/0.jpg)](https://www.youtube.com/watch?v=9nmrkG6QtpQ)
[![Binary Trees](https://img.youtube.com/vi/EPwWrs8OtfI/0.jpg)](https://www.youtube.com/watch?v=EPwWrs8OtfI)


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
