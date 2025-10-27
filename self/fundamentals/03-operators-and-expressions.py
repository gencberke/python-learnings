if __name__ == '__main__':

    # ==================== WALRUS OPERATOR (:=) ====================
    # Python 3.8+ feature: Assignment expression
    # Allows assignment and return value in a single expression
    # Java doesn't have a direct equivalent
    
    # Traditional way:
    '''
    numbers = [1, 2, 3, 4]
    count = len(numbers)
    if count > 3:
        print(f"List has {count} elements")
    '''

    # With Walrus operator (more concise):
    '''
    numbers = [1, 2, 3, 4]
    if (count := len(numbers)) > 3:  # Assigns AND checks in one line
        print(f"List has {count} elements")
    '''

    # Practical example: Reading file lines
    '''
    # Traditional way:
    line = file.readline()
    while line:
        print(line)
        line = file.readline()
    
    # With Walrus operator:
    while (line := file.readline()):
        print(line)
    '''

    # Use in list comprehensions:
    '''
    # Get squares of numbers, but only if square > 10
    numbers = [1, 2, 3, 4, 5, 6]
    
    # Without walrus:
    squares = [x*x for x in numbers if x*x > 10]
    
    # With walrus (avoids calculating x*x twice):
    squares = [square for x in numbers if (square := x*x) > 10]
    print(squares)  # Output: [16, 25, 36]
    '''


    # ==================== ARITHMETIC OPERATORS ====================
    # Python supports all standard arithmetic operators like Java
    
    '''
    x = 10
    y = 3
    
    print(x + y)   # Addition: 13
    print(x - y)   # Subtraction: 7
    print(x * y)   # Multiplication: 30
    print(x / y)   # Division: 3.333... (always returns float)
    print(x // y)  # Floor division: 3 (returns integer, rounds down)
    print(x % y)   # Modulus (remainder): 1
    print(x ** y)  # Exponentiation: 1000 (10^3)
    '''

    # IMPORTANT: Division differences from Java
    # Java: 10 / 3 = 3 (integer division)
    # Python: 10 / 3 = 3.333... (float division)
    # For integer division in Python, use //


    # ==================== COMPARISON OPERATORS ====================
    # Used to compare values, returns boolean (True/False)
    # Same as Java: ==, !=, >, <, >=, <=
    
    '''
    x = 10
    y = 5
    
    print(x == y)   # Equal to: False
    print(x != y)   # Not equal to: True
    print(x > y)    # Greater than: True
    print(x < y)    # Less than: False
    print(x >= y)   # Greater than or equal to: True
    print(x <= y)   # Less than or equal to: False
    '''


    # ==================== CHAINING COMPARISON OPERATORS ====================
    # Python allows chaining multiple comparisons
    # This is NOT possible in Java!
    
    '''
    x = 5
    
    # Instead of: (x > 0) and (x < 10)
    print(0 < x < 10)   # Output: True (much cleaner!)
    
    # More examples:
    age = 25
    print(18 <= age <= 65)  # Output: True
    
    score = 85
    print(90 <= score <= 100 or 0 <= score < 60)  # Output: False
    '''

    # Java equivalent would be:
    # if (x > 0 && x < 10) { ... }
    # Python: if 0 < x < 10: ...


    # ==================== LOGICAL OPERATORS ====================
    # Combine conditional statements
    # Python: and, or, not
    # Java: &&, ||, !
    
    '''
    # AND operator (both conditions must be True)
    print(10 < 15 and 4 > 3)   # Output: True
    print(10 < 5 and 4 > 3)    # Output: False
    
    # OR operator (at least one condition must be True)
    print(10 < 3 or 30 > 3)    # Output: True
    print(10 < 3 or 21 < 3)    # Output: False
    
    # NOT operator (reverses the result)
    print(not 30 > 10)         # Output: False
    print(not 30 < 10)         # Output: True
    '''

    # Complex logical expressions:
    '''
    age = 25
    has_license = True
    has_car = False
    
    # Can drive if: has license AND (age >= 18 OR has permission)
    can_drive = has_license and (age >= 18 or has_car)
    print(can_drive)  # Output: True
    '''

    # Short-circuit evaluation (same as Java):
    '''
    # If first condition is False, second is not checked
    x = 0
    result = (x != 0) and (10 / x > 1)  # Safe: doesn't divide by zero
    print(result)  # Output: False
    '''


    # ==================== IDENTITY OPERATORS ====================
    # Check if two variables refer to the same object in memory
    # Python: is, is not
    # Java equivalent: == for primitives, equals() for objects
    
    '''
    # 'is' checks if two variables point to the same object
    # '==' checks if two variables have the same value
    
    x = ["apple", "banana"]
    y = ["apple", "banana"]
    z = x
    
    print(x == y)   # Output: True (same values)
    print(x is y)   # Output: False (different objects in memory)
    print(x is z)   # Output: True (same object reference)
    '''

    # Practical example with numbers:
    '''
    a = 256
    b = 256
    print(a is b)  # Output: True (Python caches small integers -5 to 256)
    
    a = 257
    b = 257
    print(a is b)  # Output: False (larger numbers create new objects)
    
    # Always use '==' for value comparison, 'is' for identity
    '''

    # Common use case: Checking for None
    '''
    value = None
    
    if value is None:  # CORRECT way to check for None
        print("Value is None")
    
    # Don't use: if value == None  (works but not recommended)
    '''

    # Java comparison:
    # In Java: String s1 = "hello"; String s2 = "hello";
    #          s1 == s2 (checks reference)
    #          s1.equals(s2) (checks value)
    # In Python: s1 == s2 (checks value)
    #            s1 is s2 (checks reference)


    # ==================== MEMBERSHIP OPERATORS ====================
    # Check if a value exists in a sequence (list, tuple, string, etc.)
    # Python: in, not in
    # Java equivalent: list.contains() or string.contains()
    
    '''
    # 'in' operator
    fruits = ["apple", "banana", "cherry"]
    
    print("banana" in fruits)      # Output: True
    print("orange" in fruits)      # Output: False
    
    # 'not in' operator
    print("orange" not in fruits)  # Output: True
    print("banana" not in fruits)  # Output: False
    '''

    # With strings:
    '''
    text = "Hello World"
    
    print("World" in text)         # Output: True
    print("world" in text)         # Output: False (case-sensitive)
    print("Python" not in text)    # Output: True
    '''

    # With dictionaries (checks keys, not values):
    '''
    person = {"name": "Berke", "age": 23}
    
    print("name" in person)        # Output: True
    print("Berke" in person)       # Output: False (checks keys, not values)
    print("city" not in person)    # Output: True
    '''

    # Practical examples:
    '''
    # Check if user input is valid
    valid_choices = ["yes", "no", "maybe"]
    user_input = "yes"
    
    if user_input in valid_choices:
        print("Valid choice")
    
    # Check if character is a vowel
    vowels = "aeiou"
    char = "e"
    
    if char.lower() in vowels:
        print(f"{char} is a vowel")
    '''


    # ==================== BITWISE OPERATORS ====================
    # Operate on numbers at bit level
    # Same as Java: &, |, ^, ~, <<, >>
    
    '''
    a = 60  # Binary: 0011 1100
    b = 13  # Binary: 0000 1101
    
    print(a & b)   # AND: 12 (0000 1100)
    print(a | b)   # OR: 61 (0011 1101)
    print(a ^ b)   # XOR: 49 (0011 0001)
    print(~a)      # NOT: -61
    print(a << 2)  # Left shift: 240 (multiply by 4)
    print(a >> 2)  # Right shift: 15 (divide by 4)
    '''


    # ==================== ASSIGNMENT OPERATORS ====================
    # Assign and perform operation in one step
    
    '''
    x = 10
    
    x += 5   # x = x + 5, now x = 15
    x -= 3   # x = x - 3, now x = 12
    x *= 2   # x = x * 2, now x = 24
    x /= 4   # x = x / 4, now x = 6.0
    x //= 2  # x = x // 2, now x = 3.0
    x %= 2   # x = x % 2, now x = 1.0
    x **= 3  # x = x ** 3, now x = 1.0
    '''


    # ==================== OPERATOR PRECEDENCE ====================
    # Order of operations (same general rules as Java)
    # PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
    
    '''
    result = 10 + 5 * 2      # Output: 20 (multiplication first)
    result = (10 + 5) * 2    # Output: 30 (parentheses first)
    
    # Complete precedence (highest to lowest):
    # 1. () - Parentheses
    # 2. ** - Exponentiation
    # 3. +x, -x, ~x - Unary plus, minus, NOT
    # 4. *, /, //, % - Multiplication, Division, Floor division, Modulus
    # 5. +, - - Addition, Subtraction
    # 6. <<, >> - Bitwise shift
    # 7. & - Bitwise AND
    # 8. ^ - Bitwise XOR
    # 9. | - Bitwise OR
    # 10. ==, !=, >, <, >=, <=, is, in - Comparisons, identity, membership
    # 11. not - Logical NOT
    # 12. and - Logical AND
    # 13. or - Logical OR
    '''

    # Examples showing precedence:
    '''
    # Exponentiation before multiplication
    result = 2 * 3 ** 2      # 2 * 9 = 18, not (2*3)^2 = 36
    
    # Comparison before logical operators
    result = 5 > 3 and 10 < 20   # True and True = True
    
    # Use parentheses for clarity
    result = (5 > 3) and (10 < 20)  # More readable
    '''
