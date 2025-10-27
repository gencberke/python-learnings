import sys

if __name__ == '__main__':
    print(sys.version)

    # ======== Syntax and basics ==========
    """
    #We have to initialize a variable to use it in python
    x = 2

    # This is a comment

    print("learning python")

    # We can use ';' to separate without going for a new line
    print("we can"); print("also"); print("do it"); print("like this")

    # Added to first string at the same line with 'end'
    print("hello world", end=" finish ")
    print("hello again")

    # We can do math in print
    print(3 + 5)
    print("I am", 35, "years old")

    
    this is also a comment
    for multiple lines
    

    # Basic type casting
    y = str(3)
    a = float(3)

    print(type(y))
    print(type(a))

    b = "this is a string"
    c = 'also this is a string'

    # Snake case is recommend in python
    my_var = "this is the best practice in python to name a variable"
    
    d, e, f = "orange", "banana", "cherry"
    g = h = i = "orange"
    """

    # =========== Unpacking ===========
    """
    # Python allows to extract values into variables like this. this called unpacking
    fruits = ["apple", "banana", "cherry"]
    x, y, z = fruits
    print(x)
    print(y)
    print(z)
    """

    """
    # you can't make a string + number operation
    x = 5
    y = "hello"
    print(x + y)
    """

    # ========== Global variable ============

    """
    # Global variable example
    x = "python"

    def my_func():
        print("learning " + x)

    my_func()

    # If there is a variable named exactly same in the function then it will be used in function
    y = "python"

    def my_func():
        y = "java"
        print("learning " + y)

    my_func()
    print("learning " + y)

    # Global keyword - you can access variable globally. also you can use global if you want to change a variable which
    # is global in a function
    y = "java"

    def my_func():
        global y
        y = "python"
        print("learning " + y)

    my_func()
    print("learning " + y)
    """