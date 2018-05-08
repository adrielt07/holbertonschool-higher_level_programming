# Python - More Classes and Objects

### Challenge
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All our test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: python3 -m doctest ./tests/*
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case
- Can't import standard Modules

### Documentation
A python Class that defines a Rectangle.
Starting from 0-rectangle.py - I added more functions each file.
The description below summarieze what I added as I go.

## Python
- 0-rectangle.py - Empty class Rectangle that defines a rectangle
- 1-rectangle.py - Created a private instance width and height __init__(width=0, height=0)
- 2-rectangle.py - Added area and perimter method
- 3-rectangle.py - Added string presentation __str__ print image of rectangle with "#"
- 4-rectangle.py - Added string presentation __repr__ print "Rectangle(<width>, <height>)"
- 5-rectangle.py - Added instance deletion that print "Bye rectangle..."
- 6-rectangle.py - Added a class attribute "number_of_instances" which increments when new instance is created and decrements when del is called
- 7-rectangle.py - Added a class attribute "print_symbol" replaces the "#" symbol from 3-rectangle
- 8-rectangle.py - Added method bigger_or_equal(rect_1, rect_2) which compares the area of two rectangles and return which is bigger
- 9-rectangle.py - Final: Added square(size) method which creates a new instance with equal width and height

Usage Example from Python Interpreter:
>>> Rectangle = __import__('9-rectangle').Rectangle
>>> my_rectangle = Rectangle(2, 4)
>>> my_rectangle.area()
8
>>> my_rectangle.perimeter()
12
>>> print(str(my_rectangle))
##
##
##
##
>> my_rectangle.print_symbol = "&"
&&
&&
&&
&&
>>> repr(my_rectangle)
'Rectangle(2, 4)'

### Authors
Adriel Tolentino
