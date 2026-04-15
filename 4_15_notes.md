# Graph Algorithms
### Class Notes from 4/15/26

### Depth-First Search (DFS)

Using DFS, we can iterature through a graph using a **stack** implementation (**L**ast-**I**n-**F**irst-**O**ut). In Python, we can represent a weighted-DFS graph using two methods: a dictionary with tuples, or a nested dictionary. In a dictionary with tuples, each node would have its weight attached like so:

```python
graph = {'A': ['(B,3)'], 
         'B': ['(C,2)'],
       # and so on...
        }
```

However, the runtime for sorting to find an edge case (or to identify the cost of the edge) in the above data structure would be **O(n)** (linear).

We can also represent a weighted-DFS graph in a **nested dictionary** as shown below, also known as an ***adjacency list representation***:

```python
graph = {'A': {'B':1}, 
         'B': {'C':1},
         'C': {'A':1,'D':1},
         'D': {'F':1},
         'E': {'C':1},
         'F': {'E':1}
        }
```



<!-- to check if a vertice is strongly connected in DFS, you would run a DFS search over and over again, starting from every single vertice until you find any vertice that is unaccessible from a given starting point -->
