# Priority Queues & Heaps

## Overview: Stacks & Queues
Stacks and queues are sequence data types that allow interaction only at the end of the sequence. Operations should be implemented in ***O(1)***.
<br>
### Stacks
Stacks can be implemented using a linked list or an array list. Example applications include processing nested structures, recursion, depth-first tree traversals, etc.

**Element Processing Order:** *Last-In-First-Out* (LIFO)

| Operation | How it works |
| :-------: | :------  |
|  push(x)|add x on top of the stack (called append(x) when using Python list)|
|  pop() |return top most element remove it from the stack|
|  top() |return top most element, but don't remove it (using indexing stack[-1] when using Python list)|
|  len() |return number of elements on the stack|


 ### Queues
Queues can be implemented using a doubly linked list or a circular array (or using two stacks). Example applications include keeping track of to-do lists, simulations, breadth-first (layer-order) tree traversals, etc.

**Element Processing Order:** *First-In-First-Out* (FIFO)
| Operation | How it works |
| :-------: | :------  |
| enqueue(x)|add x at the end of the queue|
| dequeue() |return and remove the element at the front of the queue|
|  front() / peek() |return the element at the front of the queue but don't return it|
|  len() |return number of elements on the queue|

**Double Ended Queue / Deque:** combines stack and queue operations. Typically implemented using a doubly linked list; for example, `collections.deque`.

## Priority Queues

Like a stack or queue, the *Priority Queue* abstract data type has a pair of methods for inserting and retrieving elements, called `insert` and `remove_min`. In a priority queue, each element has an associated priority when inserted into the data structure. We can represent an element with its priority as a *(key,value)* pair, where the key is the priority (but note that, unlike maps, priority queues can generally contain multiple values with the same key).

<ins>Example 1:</ins> Gawain, Percivale, and Galahad arrive at a lunch buffet, waiting in line. They are all equally important (priority 10).

![King Arthur's Round Table]([URL](https://en.wikipedia.org/wiki/Round_Table#/media/File:Holy-grail-round-table-ms-fr-112-3-f5r-1470-detail.jpg))


```python
pq = SomePriorityQueue()
pq.insert((10,"Gawain"))
pq.insert((10,"Percivale"))
pq.insert((10,"Galahad"))
```
They are served in *first-come-first-serve* order before they sit down at the round table.

```python
(k,v) = pq.remove_min()  # removes and returns (10, Gawain)
(k,v) = pq.remove_min()  # removes and returns (10, Percivale)
```

All of a sudden, King Arthur walks in and cuts the line (because he is King, so he is more important).

```python
pq.insert((1,"Arthur"))
```
Before Arthur is served, Lancelot arrives (arguably the most important one of the knights, after the king).

```python
pq.insert((5,"Lancelot"))
```
Now Arthur is served, followed by Lancelot, and Galahad.

```python
(k,v) = pq.remove_min()  # this removes and returns (1,Arthur)
(k,v) = pq.remove_min()  # this removes and returns (5,Lancelot)
(k,v) = pq.remove_min()  # this removes and returns (10,Galahad)
```
The priority queue may also have a `find_min()` method to retrieve but not remove the smallest element, and a `len()` method to retrieve the number of elements in the priority queue. There are many other use cases for priority queues, such as process managment on a CPU, or prioritizing network packages by importance.

### Implementing a Priority Queue using an Unsorted List
Store the items in a list, simply append on insert, and search for minimum during lookup.

```python
class UnsortedPriorityQueue:

    class _Item:
        def __init__(self, priority,v): 
            self._priority = priority
            self._value = v
            
        def __lt__(self, other):            
            return self._priority < other._priority
    
    def __init__(self):
        self._data = [] 

    def __len__(self): 
        return len(self._data)
    
    def insert(self, priority,v): # k is the priority 
        self._data.append(self._Item(priority,v))

    def find_min(self): 
        current_smallest_index = 0 
        current_smallest_item = self._data[0]

        index = 1
        while index < len(self._data): 
            if self._data[index] < current_smallest_item:
                current_smallest_index = index 
                current_smallest_item = self._data[index]
            index += 1
            
        return current_smallest_item 

    def remove_min(self):
        current_smallest_index = 0 
        current_smallest_item = self._data[0]

        index = 1
        while index < len(self._data): 
            if self._data[index] < current_smallest_item:
                current_smallest_index = index 
                current_smallest_item = self._data[index]
            index += 1
            
        del self._data[current_smallest_index]
        return current_smallest_item
```

Given the following input:

```python
item1 = UnsortedPriorityQueue._Item(10,"Gallahad")
item2 = UnsortedPriorityQueue._Item(5, "Lancelot")
```

If you evaluate the Boolean `item2 < item1`, what will the output be?
<details>
  <summary>Answer</summary>
  True
</details>

### Video: Priority Queues Explained
[![Priority Queues Explained](https://img.youtube.com/vi/_U1AJZQxYTU/0.jpg)](https://www.youtube.com/watch?v=_U1AJZQxYTU)


