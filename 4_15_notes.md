# Depth-First Search (DFS)
### Class Notes from 4/15/26

In Python, we can represent a weighted-DFS graph using two methods: a dictionary with tuples, or a nested dictionary.

In a dictionary with tuples, each node would have its weight attached like so:

```python
graph = {'A': ['(B,3)'], 
         'B': ['(C, 2'],
       # and so on...
        }
```

+ 

+ 
+
+
+
+ Running time for find an edge case or the cost of the edge through a dictionary with weights stored in the form of tuples within a dictionary would be O(n) (linear), but sorting through a nested dictionary would be a must faster, O(1) (constant) runtime

In python, the dictionary method would be called an “adjacency list” representation
