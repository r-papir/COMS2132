# Maps & Hash Tables

**Youtube Courses:**

- [ ] *Hash Tables in 4 Minutes*
- [ ] *How Hash Tables Actually Work?*
- [ ] Finish Markdown guide

## Hash Tables
<img width="474" height="239" alt="table-10 2" src="https://github.com/user-attachments/assets/92fa93b4-a3f9-492a-8d0a-ce6d81ae5a49" />

[![Hash Tables in 4 Minutes](https://img.youtube.com/vi/knV86FlSXJ8/0.jpg)](https://www.youtube.com/watch?v=knV86FlSXJ8)
[![How Hash Tables Actually Work](https://img.youtube.com/vi/0Xv6wSguIlQ/0.jpg)](https://www.youtube.com/watch?v=0Xv6wSguIlQ)


## Maps

| Operation | How it works |
| :---: | :--- |
| Left-aligned | Center-aligned |
| Row 2 | Data |

Map Abstract Data Type (ADT) should support all the behaviors that Python's built-in dict class supports. The most significant five methods/behaviors are:

get(key): return the value associated with a given key in a map if one exists or raise a KeyError if such value does not exist
set(key, value): set the value for a given key to a given value. If a given key is already in a map, replace it's current value with the given value
remove(key): remove the key and its associated value.
len: return the number of key/value pairs in a map
Additionally, a map should support behaviors such as iterating through the keys, values, key-value pairs, but we will focus on the essentials.

Note: The map ADT does not specify any requirements on the keys or values -- but specific data structure implementations may.

Python already defines an abstract based class for the map ADT:
