import sys

if __name__ == '__main__':
    print(sys.version)

    # ==================== SYNTAX AND BASICS ====================
    
    # Variables must be initialized before use in Python
    '''
    x = 2
    print(x)  # Output: 2
    '''

    # This is a single-line comment
    # Python uses '#' for comments (similar to '//' in Java)

    '''
    print("learning python")
    '''

    # Using semicolon ';' to separate statements on the same line
    # Note: This is possible but NOT recommended in Python (unlike Java where it's required)
    '''
    print("we can"); print("also"); print("do it"); print("like this")
    '''

    # The 'end' parameter controls what's printed at the end
    # By default, print() adds a newline, but we can change it
    '''
    print("hello world", end=" finish ")  # Adds " finish " instead of newline
    print("hello again")
    # Output: hello world finish hello again
    '''

    # Python can perform math operations directly in print
    '''
    print(3 + 5)                      # Output: 8
    print("I am", 35, "years old")    # Output: I am 35 years old
    '''

    # Multi-line comments using triple quotes
    # Note: This is actually a multi-line string, not a true comment
    '''
    This is a multi-line comment.
    You can write multiple lines here.
    Python will ignore this if it's not assigned to a variable.
    '''

    # ==================== TYPE CASTING ====================
    # Converting between different data types
    
    '''
    y = str(3)      # Convert int to string: "3"
    a = float(3)    # Convert int to float: 3.0

    print(type(y))  # Output: <class 'str'>
    print(type(a))  # Output: <class 'float'>
    '''

    # ==================== STRING DECLARATIONS ====================
    # Both single and double quotes work for strings
    
    '''
    b = "this is a string"
    c = 'also this is a string'
    
    # Use single quotes when string contains double quotes, and vice versa
    message = "He said 'Hello'"
    greeting = 'She said "Hi"'
    '''

    # ==================== NAMING CONVENTIONS ====================
    # Python recommends snake_case for variable names
    # Java uses camelCase: myVariableName
    # Python uses snake_case: my_variable_name
    
    '''
    my_var = "this is the best practice in python to name a variable"
    user_name = "berke"
    total_count = 100
    '''

    # Multiple assignment - assigning multiple variables in one line
    '''
    d, e, f = "orange", "banana", "cherry"
    print(d)  # Output: orange
    print(e)  # Output: banana
    print(f)  # Output: cherry
    '''

    # Assigning the same value to multiple variables
    '''
    g = h = i = "orange"
    print(g)  # Output: orange
    print(h)  # Output: orange
    print(i)  # Output: orange
    '''


    # ==================== UNPACKING ====================
    # Python allows extracting values from collections into variables
    # This is similar to destructuring in modern Java (Java 14+)
    
    '''
    fruits = ["apple", "banana", "cherry"]
    x, y, z = fruits  # Unpacking the list
    
    print(x)  # Output: apple
    print(y)  # Output: banana
    print(z)  # Output: cherry
    '''

    # Unpacking with tuples
    '''
    coordinates = (10, 20, 30)
    x, y, z = coordinates
    print(f"X: {x}, Y: {y}, Z: {z}")  # Output: X: 10, Y: 20, Z: 30
    '''

    # Partial unpacking with * operator
    '''
    numbers = [1, 2, 3, 4, 5]
    first, *middle, last = numbers
    print(first)   # Output: 1
    print(middle)  # Output: [2, 3, 4]
    print(last)    # Output: 5
    '''


    # ==================== TYPE MIXING RESTRICTIONS ====================
    # IMPORTANT: You cannot directly concatenate strings and numbers
    # In Java: "hello" + 5 automatically converts to "hello5"
    # In Python: This causes a TypeError!
    
    '''
    x = 5
    y = "hello"
    # print(x + y)  # ERROR: TypeError: unsupported operand type(s)
    
    # SOLUTIONS:
    print(str(x) + y)      # Convert to string: "5hello"
    print(y, x)            # Use comma: "hello 5"
    print(f"{y} {x}")      # Use f-string: "hello 5"
    '''


    # ==================== GLOBAL VARIABLES ====================
    # Variables defined outside functions are global
    
    '''
    x = "python"

    def my_func():
        print("learning " + x)  # Can access global x

    my_func()  # Output: learning python
    '''

    # Local variable shadows global variable
    # If a variable with the same name exists in the function, it's used instead
    '''
    y = "python"

    def my_func():
        y = "java"  # This is a LOCAL variable, not the global one
        print("learning " + y)

    my_func()           # Output: learning java
    print("learning " + y)  # Output: learning python (global unchanged)
    '''

    # Using 'global' keyword to modify global variables inside functions
    # Similar to how you'd handle static variables in Java
    '''
    y = "java"

    def my_func():
        global y       # Declare that we want to use the global variable
        y = "python"   # Now this modifies the global variable
        print("learning " + y)

    my_func()              # Output: learning python
    print("learning " + y)  # Output: learning python (global changed)
    '''

    # Example: Counter using global variable
    '''
    counter = 0

    def increment():
        global counter
        counter += 1
        return counter

    print(increment())  # Output: 1
    print(increment())  # Output: 2
    print(increment())  # Output: 3
    '''

    # Best Practice: Avoid global variables when possible
    # Instead, use function parameters and return values
    '''
    def increment_counter(count):
        return count + 1

    counter = 0
    counter = increment_counter(counter)  # Better approach
    print(counter)  # Output: 1
    '''
