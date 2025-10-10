if __name__ == '__main__':

    # ==================== 1) INDENTATION ====================
    # Python uses indentation (spaces/tabs) to define code blocks.
    # Instead of curly braces {} like Java, Python uses indentation!
    
    # In Java:
    # if (5 > 1) {
    #     System.out.println("true");
    # } else {
    #     System.out.println("false");
    # }
    
    # In Python (CORRECT):
    '''
    if 5 > 1:
        print("true")
    else:
        print("false")
    '''

    # In Python (WRONG - will cause error):
    '''
    if 5 > 1:
        print("true")
                else: print("false")  # else is incorrectly indented
    '''


    # ==================== 2) VARIABLES ====================
    # Python has dynamic typing - you don't need to specify types!
    # In Java: String x = "ali"; int y = 23;
    # In Python: x = "ali" and y = 23 is enough!
    
    # Basic data types in Python:
    # - str (String): Text data, example: "Hello"
    # - int (Integer): Whole numbers, example: 42
    # - float (Float): Decimal numbers, example: 3.14
    # - bool (Boolean): True or False
    # - complex (Complex number): Example: 3+5j
    
    '''
    x = "ali"           # str type
    y = 23              # int type
    print(x)
    print(y)
    '''

    # camelCase naming (Python generally prefers snake_case but both work):
    '''
    nameSurname = "berke genc"
    print(nameSurname)
    '''

    # snake_case is more common in Python:
    '''
    name_surname = "berke genc"
    print(name_surname)
    '''

    # Multiple assignment - assigning values to multiple variables at once:
    '''
    x, y, z = 1, 2, 3
    print(x, y, z)  # Output: 1 2 3
    '''

    # String concatenation:
    '''
    nameSurname = "berke" + " genc"
    print(nameSurname)  # Output: berke genc
    '''

    # Printing strings and different types:
    '''
    nameSurname = "berke" + " genc"
    work = "student"
    print("this person: " + nameSurname + " -> ", work)
    '''

    # IMPORTANT: In Python, int cannot be directly concatenated with String!
    # In Java: "text" + 10 works (automatically converts to string)
    # In Python: "text" + 10 causes TypeError!
    
    # WRONG (causes error):
    '''
    nameSurname = "berke" + " genc"
    point = 10
    print(nameSurname + point)  # TypeError!
    '''

    # CORRECT (using comma to print different types):
    '''
    nameSurname = "berke" + " genc"
    point = 10
    print(nameSurname, " -> ", point)  # Using comma allows printing different types
    '''

    # CORRECT (converting to string):
    '''
    nameSurname = "berke" + " genc"
    point = 10
    print(nameSurname + " -> " + str(point))  # Convert int to string using str()
    '''


    # ==================== TYPE CASTING ====================
    # In Java: (float) x or Float.parseFloat()
    # In Python: Use functions like float(x), int(x), str(x)
    
    '''
    x = 10              # int
    print(x)
    
    x = float(10)       # Convert int to float
    print(x)            # Output: 10.0
    
    x = 10.1            # float
    print(x)
    
    x = int(10.5)       # Convert float to int (decimal part is truncated)
    print(x)            # Output: 10
    '''

    # Defining complex numbers:
    # Python supports complex numbers for mathematical calculations
    '''
    x = 1j              # Define complex number with j or J
    print(x)            # Output: 1j
    print(type(x))      # Output: <class 'complex'>
    '''


    # ==================== 3) FUNCTIONS ====================
    # In Java: public void myfunc() { ... }
    # In Python: def myfunc(): ...
    
    # Simple function definition:
    '''
    def myfunc():
        print("myfunc")
    
    myfunc()  # Call the function
    '''

    # Using global variables inside functions:
    '''
    x = 2

    def myfunc():
        print("myfunc", x)  # We can read global x (read-only)
    
    myfunc()  # Output: myfunc 2
    '''

    # Defining local variables inside functions:
    '''
    x = 2  # Global x

    def myfunc():
        x = 3  # Local x (only valid inside function)
        print("myfunc", x)  # Output: myfunc 3
    
    myfunc()
    print("global x:", x)  # Output: global x: 2 (global x unchanged)
    '''

    # Using global keyword to modify global variable inside function:
    '''
    def myfunc():
        global x  # Declare x as global
        x = 2     # Assign value to global x
        print("myfunc", x)  # Output: myfunc 2
        x = 3     # Modify global x
        print("myfunc", x)  # Output: myfunc 3
    
    myfunc()
    print("after function:", x)  # Output: after function: 3
    '''

    # type() function - checking variable type:
    # In Java: We use checks like x instanceof Integer
    # In Python: We can use type(x) to check the type
    '''
    x = 10
    print(type(x))      # Output: <class 'int'>
    
    y = 1j
    print(type(y))      # Output: <class 'complex'>
    
    z = "hello"
    print(type(z))      # Output: <class 'str'>
    '''


    # ==================== 4) LIST, TUPLE and RANGE ====================
    
    # LIST - Mutable (can be modified):
    # Similar to ArrayList in Java. Elements can be added or removed.
    # Defined with square brackets [].
    '''
    fruits = ["apple", "banana", "cherry"]
    print(fruits)           # Output: ['apple', 'banana', 'cherry']
    
    fruits.append("orange") # Add element
    print(fruits)           # Output: ['apple', 'banana', 'cherry', 'orange']
    
    fruits[0] = "grape"     # Modify first element
    print(fruits)           # Output: ['grape', 'banana', 'cherry', 'orange']
    
    print(fruits[1])        # Access by index - Output: banana
    '''

    # TUPLE - Immutable (cannot be modified):
    # No direct equivalent in Java. Think of it as a constant array.
    # Defined with parentheses ().
    '''
    numbers = (1, 2, 3)
    print(numbers)          # Output: (1, 2, 3)
    print(numbers[0])       # Output: 1
    
    # numbers[0] = 5        # ERROR! Tuple cannot be modified
    '''

    # When to use LIST vs TUPLE?
    # - LIST: When data will change (e.g., shopping list)
    # - TUPLE: When data should remain constant (e.g., coordinates (x, y))

    # RANGE - Creating number sequences:
    # Think of it like for(int i=0; i<5; i++) in Java
    # range() creates a sequence of numbers without taking up memory
    '''
    x = range(5)            # Numbers from 0 to 4 (5 is not included!)
    print(x)                # Output: range(0, 5)
    print(list(x))          # Output: [0, 1, 2, 3, 4]
    
    y = range(2, 8)         # From 2 to 7
    print(list(y))          # Output: [2, 3, 4, 5, 6, 7]
    
    z = range(0, 10, 2)     # From 0 to 10, incrementing by 2
    print(list(z))          # Output: [0, 2, 4, 6, 8]
    '''

    # Range is commonly used in for loops:
    '''
    for i in range(5):
        print(i)  # Prints 0, 1, 2, 3, 4
    '''


    # ==================== 5) DICTIONARY ====================
    # Similar to HashMap in Java - key-value pairs
    # Defined with curly braces {}
    
    '''
    person = {"name": "Berke", "age": 23, "city": "Istanbul"}
    print(person)                   # Print entire dictionary
    
    print(person["name"])           # Access value by key - Output: Berke
    print(person.get("age"))        # Access using get() method - Output: 23
    
    person["job"] = "student"       # Add new key-value pair
    print(person)
    
    person["age"] = 24              # Update existing value
    print(person)
    '''

    # Dictionary methods:
    '''
    x = {"name": "Berke", "number": 3}
    
    print(x.keys())     # Get all keys - Output: dict_keys(['name', 'number'])
    print(x.values())   # Get all values - Output: dict_values(['Berke', 3])
    print(x.items())    # Get key-value pairs
    '''

    # Java comparison:
    # Java: HashMap<String, Object> map = new HashMap<>();
    #       map.put("name", "Berke");
    # Python: x = {"name": "Berke"}
