'''Initializing any class:'''

# Declares a new class with a constructer
class SomeClass:
  def __init__(self, some_attribute):
    self.some_attribute = some_attribute
# Use this when you want to store initial state of the object if you need to pass on that data somewhere else later
# Don't need to use this when you're inheriting from a parent class whose __init__ already handles this

# ---------------------------------------------------------

class Node:

    # init function
    def __init__(self, value, link_node = None):
        self.value = value
        self.link_node = link_node

    # Define the get_value and get_link_node methods:
    def get_value(self):
        return self.value

    def get_link_node(self):
        return self.link_node
  
    # Define your set_link_node method:
    def set_link_node(self, link_node):
        self.link_node = link_node

yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

dot.set_link_node(wacko)
yacko.set_link_node(dot)

dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()

print(dots_data)
print(wackos_data)

# ---------------------------------------------------------

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
# Add your insert_beginning and stringify_list methods below:

  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
    # Define your remove_node method below:
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:

# TEST
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())