# Data Structures: Priority Queues & Heaps

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
