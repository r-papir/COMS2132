## Abstract Data Types: Trees

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