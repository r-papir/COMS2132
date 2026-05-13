# Heap Data Structure

## Overview: Stacks & Queues
Stacks and queues are sequence data types that allow interaction only at the end of the sequence. Operations should be implemented in ***O(1)***.
<br>
### Stacks
Stacks can be implemented using a linked list or an array list. Example applications include processing nested structures, recursion, depth-first tree traversals, etc.
**Element Processing Order:** Last-In-First-Out (LIFO)

**Operations:**

<details> <summary>push(x)</summary>
  <br>
  add x on top of the stack (called append(x) when using Python list)
</details>

<details> <summary>pop()</summary>
  <br>
  return top most element remove it from the stack
</details>

<details> <summary>top()</summary>
  <br>
   return top most element, but don't remove it (using indexing stack[-1] when using Python list)
</details>

<details> <summary>len()</summary>
  <br>
   return number of elements on the stack
</details>

<details> <summary>len()</summary>
  <br>
   return number of elements on the stack
</details>

 

 



Queue: First-In-First-Out (FIFO)

enqueue(x) add x at the end of the queue.
dequeue() return and remove the element at the front of the queue.
front()/peek() return the element at the front of the queue but don't return it.
len() return number of elements on the queue.
Queues can be implemented using a doubly linked list or a circular array (or using two stacks).

Applications: keeping track of to-do lists, simulations, breadth-first (layer-order) tree traversals, ...

Double Ended Queue / Deque: combines stack and queue operations. Typically implemented using a doubly linked list. For example collections.deque.
