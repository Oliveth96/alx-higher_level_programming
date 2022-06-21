0x05. Python - Exceptions


Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
What’s the difference between errors and exceptions
What are exceptions and how to use them
When do we need to use exceptions
How to correctly handle an exception
What’s the purpose of catching exceptions
How to raise a builtin exception
When do we need to implement a clean-up action after an exception


FILES
0-safe_print_list.py; Writes a function that prints x elements of a list.

1-safe_print_integer.py; Write a function that prints an integer with "{:d}".format().


2-safe_print_list_integers.py;Writes a function that prints the first x elements of a list and only integers.
Prototype: def safe_print_list_integers(my_list=[], x=0):


3-safe_print_division.py; Writes a function that divides 2 integers and prints the result.
Prototype: def safe_print_division(a, b):


4-list_division.py; Writes a function that divides element by element 2 lists.
Prototype: def list_division(my_list_1, my_list_2, list_length):


5-raise_exception.py; Writes a function that raises a type exception.
Prototype: def raise_exception():


6-raise_exception_msg.py; Writes a function that raises a name exception with a message.
Prototype: def raise_exception_msg(message=""):


100-safe_print_integer_err.p; Writes a function that prints an integer.
Prototype: def safe_print_integer_err(value):


101-safe_function.py; Writes a function that executes a function safely.
Prototype: def safe_function(fct, *args):


102-magic_calculation.py; Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:


103-python.c;
Python lists:

Prototype: void print_python_list(PyObject *p);
Format: see example
If p is not a valid PyListObject, print an error message (see example)
Python bytes:

Prototype: void print_python_bytes(PyObject *p);
Format: see example
Line “first X bytes”: print a maximum of 10 bytes
If p is not a valid PyBytesObject, print an error message (see example)
Python float:

Prototype: void print_python_float(PyObject *p);
Format: see example
If p is not a valid PyFloatObject, print an error message (see example)
Read /usr/include/python3.4/floatobject.h  