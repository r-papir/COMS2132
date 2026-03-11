# Data Structures: Operations

In Python, some basic operations we can do on elements in a data structure (specifically, arrays) include **integer indexing**, **insertion**, **removal**, and **appendation**. This guide will expand on more operations we can implement using *imported modules*.

## Vocabulary

**DeepCopy:** a built-in function in Python that creates a completely independent clone of an object, including all objects it refers to, recursively

**NumPy:** a standard package for numeric computing in Python

+ The basic data type in is the numpy *n-dimensional* array; these can be used to represent *vectors* (1D), *matrices* (2D), or *tensors* (nD)

Read more about *Shallow and Deep Copy Operations* [**here**](https://docs.python.org/3/library/copy.html).

**Array:** a linear datatype and structure that stores elements of the *same* datatype in contiguous memory locations

+ **Matrix:** a arbitrary multidimensional array (e.g. a tic-tac-toe board)

+ **Referential Array:** elements ("references") are stored in a contiguous block of memory, and but the actual data objects are scattered and not necessarily next to each other → elements stored as contiguous sequence of *references* to themselves, rather than storing the actual elements directly

<br>

For representing multidimensional data, we would use a *matrix*, but the underlying structure of matrices still stores elements in the form of a *referential array*:

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

```python
li = [1,2,3]

# shallow copy
test = li

# deep copy  
test = li[:]

x = [1,2,3]
y = [4,5,6]
z = [7,8,9]

li = [x,y,z]
test = li 

# shallow copy - inner lists are not duplicated 
li2 = li[:] 


li[0][0] = 0 
li
```

### Multidimensional arrays are made much simpler by using the *NumPy* module:
```python
# Creating multidimensional arrays using numpy.array is straightforward
matrix = numpy.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

# See the result
print(matrix)
type(matrix)

```
+ 1-dimensional NumPy arrays are often used to represent a series of data
+ n-dimensional arrays often represent complete data sets (each column is a type of measurement)
+ NumPy arrays are very similar to Python lists because indexing and slicing works the same way (including assingments); unlike a Python list, however, all cells in the same NumPy array must contain the same data type

Many Python built-in operators have been overloaded for NumPy arrays to make working with vectors, matrices, and tensors easy. Because of this, it's also easy to compute descriptive statistics for a series of data:
```python
u.max(), u.min(), u.mean(), u.std() # maximum, minimum, mean, standard deviation
```
The parameter **dtype="uint64"** tells NumPy what data types cells should use. NumPy arrays are homogeneous, and each cell has a maximum value that it can store which is determined by the data type.
```python
rows = 4
cols = 3
matrix = numpy.zeros((rows, cols), dtype="uint8") # row x col matrix filled with zeros

print(matrix)
#matrix[2][0] = 42
matrix[2,0] = 255
print(matrix)
```

We can create an array using *literals* (notation in the source code that represents a fixed data value directly):
```python
# Create a double array directly using literals
m = numpy.array([[1,2,3]])
m.shape
```
```python
# Create a single array directly using literals
m = numpy.array([1,2,3])
m.shape
```
And then, we can create a vector and reshape the array in different ways:
```python
# Create a vector and reshape
m = numpy.array(range(27))
m

# OUTPUT: array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
#       17, 18, 19, 20, 21, 22, 23, 24, 25, 26])
```
```python
m2 = m.reshape((3,3,3))
m2

'''OUTPUT: array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8]],

       [[ 9, 10, 11],
        [12, 13, 14],
        [15, 16, 17]],

       [[18, 19, 20],
        [21, 22, 23],
        [24, 25, 26]]])
'''
```

Learn more about the NumPy module [**here**](https://numpy.org/).