0x07. Python - Test-driven development


Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
What’s an interactive test
Why tests are important
How to write Docstrings to create tests
How to write documentation for each module and function
What are the basic option flags to create tests
How to find edge cases



FILES:
0-add_integer.py, tests/0-add_integer.txt; Write a function that adds 2 integers.
Prototype: def add_integer(a, b=98)


2-matrix_divided.py, tests/2-matrix_divided.txt; Write a function that divides all elements of a matrix.
Prototype: def matrix_divided(matrix, div)


3-say_my_name.py, tests/3-say_my_name.txt; Write a function that prints My name is <first name> <last name>
Prototype: def say_my_name(first_name, last_name="")



4-print_square.py, tests/4-print_square.txt; Write a function that prints a square with the character #.
Prototype: def print_square(size)



5-text_indentation.py, tests/5-text_indentation.txt; Write a function that prints a text with 2 new lines after each of these characters: ., ? and :
Prototype: def text_indentation(text)



tests/6-max_integer_test.py; Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.
In this task, you will write unittests for the function def max_integer(list=[])



100-matrix_mul.py, tests/100-matrix_mul.txt; Write a function that multiplies 2 matrices:
Prototype: def matrix_mul(m_a, m_b):



101-lazy_matrix_mul.py, tests/101-lazy_matrix_mul.txt; Write a function that multiplies 2 matrices by using the module NumPy
To install it: pip3 install numpy==1.15.0
Prototype: def lazy_matrix_mul(m_a, m_b):



102-python.c; Create a function that prints Python strings.
Prototype: void print_python_string(PyObject *p);