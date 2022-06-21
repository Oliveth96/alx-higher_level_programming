0x06. Python - Classes and Objects
Python
OOP

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
What is OOP
“first-class everything”
What is a class
What is an object and an instance
What is the difference between a class and an object or instance
What is an attribute
What are and how to use public, protected and private attributes
What is self
What is a method
What is the special __init__ method and how to use it
What is Data Abstraction, Data Encapsulation, and Information Hiding
What is a property
What is the difference between an attribute and a property in Python
What is the Pythonic way to write getters and setters in Python
How to dynamically create arbitrary new attributes for existing instances of a class
How to bind attributes to object and classes
What is the __dict__ of a class and/or instance of a class and what does it contain
How does Python find the attributes of an object or class
How to use the getattr function


FILES:
0-square.py; Write an empty class Square that defines a square:
You are not allowed to import any module


1-square.py; Write a class Square that defines a square by: (based on 0-square.py)
Private instance attribute: size
Instantiation with size (no type/value verification)


2-square.py; Write a class Square that defines a square by: (based on 1-square.py)
Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0)


3-square.py; Write a class Square that defines a square by: (based on 2-square.py)
Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0)


4-square.py; Write a class Square that defines a square by: (based on 3-square.py)
Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it


5-square.py; Write a class Square that defines a square by: (based on 4-square.py)
Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
Instantiation with optional size: def __init__(self, size=0)


6-square.py; Write a class Square that defines a square by: (based on 5-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:
Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #

ADVANCED TASKS
100-singly_linked_list.py; Write a class Node that defines a node of a singly linked list by:

Private instance attribute: data:
property def data(self): to retrieve it
property setter def data(self, value): to set it:
Private instance attribute: next_node:
property def next_node(self): to retrieve it
property setter def next_node(self, value): to set it:
Instantiation with data and next_node: def __init__(self, data, next_node=None):

And, write a class SinglyLinkedList that defines a singly linked list by:

Private instance attribute: head (no setter or getter)
Simple instantiation: def __init__(self):
Public instance method: def sorted_insert(self, value)




101-square.py; Write a class Square that defines a square by: (based on 6-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:

Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:

Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #



102-square.py; Write a class Square that defines a square by: (based on 4-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:

Instantiation with size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area Square




<b>103-magic_class.py<b>; Write the Python class MagicClass that does exactly the same as the following Python bytecode: