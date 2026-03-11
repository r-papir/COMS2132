**Array:** a linear datatype and structure that stores elements of the same data type in contiguous memory locations
**Tuple:** a datatype representing an ordered, immutable (unchangeable) collection of elements
**List:** a built-in datatype in python based on arrays; holds elements of different data types
**Matrix:** a arbitrary multidimensional array
**Vector:** an array that can change in size dynamically during runtime
**Linked List:** a type of list where the elements (nodes) are scattered throughout memory and linked by 'pointers'

*Visualization of a linked list:*
![comparison of built-in Python list structure to linked list structure](linked_list.png)



```python
# The correct way to create a matrix
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