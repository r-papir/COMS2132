# Priority Queues & Heaps

## Overview: Stacks & Queues
Stacks and queues are sequence data types that allow interaction only at the end of the sequence. Operations should be implemented in ***O(1)***.
<br>
### Stacks
Stacks can be implemented using a linked list or an array list. Example applications include processing nested structures, recursion, depth-first tree traversals, etc.

**Processing Order:** *Last-In-First-Out* (LIFO)

| Operation | How it works |
| :-------: | :------  |
|  push(x)|add x on top of the stack (called append(x) when using Python list)|
|  pop() |return top most element remove it from the stack|
|  top() |return top most element, but don't remove it (using indexing stack[-1] when using Python list)|
|  len() |return number of elements on the stack|


 ### Queues
Queues can be implemented using a doubly linked list or a circular array (or using two stacks). Example applications include keeping track of to-do lists, simulations, breadth-first (layer-order) tree traversals, etc.

**Processing Order:** *First-In-First-Out* (FIFO)
| Operation | How it works |
| :-------: | :------  |
| enqueue(x)|add x at the end of the queue|
| dequeue() |return and remove the element at the front of the queue|
|  front() / peek() |return the element at the front of the queue but don't return it|
|  len() |return number of elements on the queue|

**Double Ended Queue / Deque:** combines stack and queue operations. Typically implemented using a doubly linked list; for example, `collections.deque`.

## Priority Queues

Like a stack or queue, the *Priority Queue* abstract data type has a pair of methods for inserting and retrieving elements, called `insert` and `remove_min`. In a priority queue, each element has an associated priority when inserted into the data structure. We can represent an element with its priority as a *(key,value)* pair, where the key is the priority (but note that, unlike maps, priority queues can generally contain multiple values with the same key).

<p><a href="https://commons.wikimedia.org/wiki/File:Holy-grail-round-table-ms-fr-112-3-f5r-1470-detail.jpg#/media/File:Holy-grail-round-table-ms-fr-112-3-f5r-1470-detail.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/6/62/Holy-grail-round-table-ms-fr-112-3-f5r-1470-detail.jpg" alt="Holy-grail-round-table-ms-fr-112-3-f5r-1470-detail.jpg" height="332" width="354"></a><br><em>By <a href="https://en.wikipedia.org/wiki/Evrard_d%27Espinques" class="extiw" title="w:Evrard d'Espinques">Evrard d'Espinques</a> - <a rel="nofollow" class="external text" href="http://gallica.bnf.fr/ark:/12148/btv1b8527589h/f13.item">Gallica</a>, Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=24915213">Link</a></p></em>

**<ins>Example 1:</ins>** Gawain, Percivale, and Galahad arrive at a lunch buffet, waiting in line. They are all equally important (priority 10).
```python
pq = SomePriorityQueue()   # create the priority queue
pq.insert((10,"Gawain"))   # insert Sir Gawain, with a priority of 10
pq.insert((10,"Percivale"))   # insert Sir Percivale, with a priority of 10
pq.insert((10,"Galahad"))    # insert Sir Galahad, with a priority of 10
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
Before King Arthur is served, Sir Lancelot arrives (arguably the most important one of the knights, after the king).

```python
pq.insert((5,"Lancelot"))
```
Now King Arthur is served, followed by Sir Lancelot, and then Sir Galahad.

```python
(k,v) = pq.remove_min()  # this removes and returns (1,Arthur)
(k,v) = pq.remove_min()  # this removes and returns (5,Lancelot)
(k,v) = pq.remove_min()  # this removes and returns (10,Galahad)
```
The priority queue may also have a `find_min()` method to retrieve but not remove the smallest element, and a `len()` method to retrieve the number of elements in the priority queue. There are many other use cases for priority queues, such as process managment on a CPU, or prioritizing network packages by importance.

### Implementing a Priority Queue using an Unsorted List
Store the items in a list, simply append on insert, and search for minimum during lookup.

| Operation | Runtime |
| :-------: | :------: |
| insert()  | O(1) amortized |
| find_min()  | O(n)  |
| remove_min()  | O(n)  |

Try looking for these operations in the program below. Can you find them?
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
**Practice:** Given the following input:

```python
item1 = UnsortedPriorityQueue._Item(10,"Gallahad")
item2 = UnsortedPriorityQueue._Item(5, "Lancelot")
```
If you evaluate the Boolean `item2 < item1`, what will the output be?
<details>
  <summary>Answer</summary>
  True
</details>
<br>

**Video 1 (left):** *Priority Queues in 8 Minutes* (Optional)

**Video 2 (right):** *Transition from Priority Queues to Heaps*

[![Priority Queues in 8 Minutes](https://img.youtube.com/vi/wRvOzgt2ygs/0.jpg)](https://www.youtube.com/watch?v=wRvOzgt2ygs) [![Priority Queues to Heaps](https://img.youtube.com/vi/yntfI_jqNms/0.jpg)](https://www.youtube.com/watch?v=yntfI_jqNms)


___

## Binary Heaps

Instead of a list, we can store the items (with their priorities) in a *binary heap*. The heap guarantess ***O(log n)*** insertion time and ***O(log n)*** runtime for find_min / remove_min. It stores the items in a complete binary tree, stored in an array. A binary heap is a complete binary tree in which the keys stored in the nodes satisfy the heap order property:

**<ins>Recall that...</ins>**
+ In a complete binary tree with height *h*, levels 0, 1, 2, ..., *h*-1 have the maximum number of nodes.
+ On level *h*, all nodes are in the leftmost possible position at that level.
+ A complete binary tree can be stored in an array (with the root at index 1, and index 0 left empty).
+ For a node at position *i* (other than the root), its parent is in position ***i*//2**.
+ For a node at position *i*, its left child is in position **2*i*** and its right child in position **2*i*+1**.
+ For every node *p* other than the root, the key stored at *p* is greater than or equal to the key stored at *p*'s parents.




**Supplemental Videos:**

[![Heaps in 3 Minutes](https://img.youtube.com/vi/0wPlzMU-k00/0.jpg)](https://www.youtube.com/watch?v=0wPlzMU-k00) [![Heaps & Priority Queues](https://img.youtube.com/vi/E2v9hBgG6gE/0.jpg)](https://www.youtube.com/watch?v=E2v9hBgG6gE) [![Heaps & Priority Queues](https://img.youtube.com/vi/E2v9hBgG6gE/0.jpg)](https://www.youtube.com/watch?v=E2v9hBgG6gE) [![Priority Queue Introduction](https://img.youtube.com/vi/wptevk0bshY/0.jpg)](https://www.youtube.com/watch?v=wptevk0bshY)

<!-- [![Alt text for image](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID) -->


