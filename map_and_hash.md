# Maps, Hash Functions, and Hash Tables

**Tutorials & Courses:**

- [ ] *How Hash Tables Actually Work?*
- [ ] *Hash Maps in Python*
- [ ] *Hash  Tables, Sets, and Maps*
- [ ] *[Introduction to Hashing](https://www.geeksforgeeks.org/dsa/introduction-to-hashing-2/)*

### Hash Tables
**Dictionary:** a generic structure for mapping key values
**Hash Table:** implementation of a dictionary using a *hash function*
<br>

**Runtime per hash operation:**
<img width="474" height="239" alt="table-10 2" src="https://github.com/user-attachments/assets/92fa93b4-a3f9-492a-8d0a-ce6d81ae5a49" />

[![How Hash Tables Actually Work](https://img.youtube.com/vi/0Xv6wSguIlQ/0.jpg)](https://www.youtube.com/watch?v=0Xv6wSguIlQ)
[![Hash Maps in Python](https://img.youtube.com/vi/RcZsTI5h0kg/0.jpg)](https://www.youtube.com/watch?v=RcZsTI5h0kg)
[![Hash Tables, Sets, and Maps](https://img.youtube.com/vi/iZyxNEBpqFY/0.jpg)](https://www.youtube.com/watch?v=iZyxNEBpqFY)




## Maps

| Operation | Runtime (Avg.; Worst) | How it works |
| :---: | :--- |  :--- |
| insert | O(1); O(n)  | |
| delete | Data | |
| search | Data | |

Map Abstract Data Type (ADT) should support all the behaviors that Python's built-in dict class supports. The most significant five methods/behaviors are:

get(key): return the value associated with a given key in a map if one exists or raise a KeyError if such value does not exist
set(key, value): set the value for a given key to a given value. If a given key is already in a map, replace it's current value with the given value
remove(key): remove the key and its associated value.
len: return the number of key/value pairs in a map
Additionally, a map should support behaviors such as iterating through the keys, values, key-value pairs, but we will focus on the essentials.

Note: The map ADT does not specify any requirements on the keys or values -- but specific data structure implementations may.

Python already defines an abstract based class for the map ADT:
