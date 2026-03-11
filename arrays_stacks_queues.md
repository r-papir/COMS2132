## Data Structures: Arrays

**Array:** a linear datatype and structure that stores elements of the *same* datatype in contiguous memory locations

+ **Referential Array:** elements ("references") are stored in a contiguous block of memory, and but the actual data objects are scattered and not necessarily next to each other

+ **Dynamic Array:** an array that can grow or shrink in size automatically at runtime, as elements are added or removed

+ **Static Array:** the actual data elements are stored in a single, contiguous block of memory

+ **Compact Array:** stores the actual data values directly next to each other in a contiguous block

+ **Matrix:** a arbitrary multidimensional array

**Tuple:** a datatype representing an ordered, immutable (unchangeable) collection of elements

**List:** a built-in datatype in python based on arrays that holds elements of *different* data types

**Vector:** an array that can change in size dynamically during runtime

**Linked List:** a type of list where the elements (nodes) are scattered throughout memory and linked by 'pointers'

+ **Singly Linked List:** text here...

+ **Doubly Linked List:** text here...

<br>

*Visualization of a linked list:*
![comparison of built-in Python list structure to linked list structure](linked_list.png)


#### The correct way to create a matrix:
```python
from copy import deepcopy

def make_matrix(col, row):
    return [[0] * col for j in range(row)]

new_row = [0] * col
matrix = []
for j in range(row): 
    my_row = deepcopy(new_row)
    matrix.append(my_row)

matrix = make_matrix(5,3)

# Let's try to modify a single cell within the matrix
matrix[2][0] = 42

# Print the matrix to see the result
print(matrix)
```
