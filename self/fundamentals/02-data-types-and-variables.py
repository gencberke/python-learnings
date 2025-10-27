import sys
import random

if __name__ == '__main__':
    print(sys.version)

    # ==================== BUILT-IN DATA TYPES ====================

    # Text Type:      str (string)
    # Numeric Types:  int, float, complex
    # Sequence Types: list, tuple, range
    # Mapping Type:   dict (dictionary)
    # Set Types:      set, frozenset
    # Boolean Type:   bool
    # Binary Types:   bytes, bytearray, memoryview
    # None Type:      NoneType

    # Examples of setting different data types:
    '''
    a = 20.5                                      # float
    b = 1j                                        # complex
    c = ["apple", "banana", "cherry"]             # list
    d = ("a", "b", "c")                           # tuple
    e = range(6)                                  # range
    f = {"name": "John", "age": 18}               # dict
    g = {"apple", "banana", "cherry"}             # set
    h = frozenset({"apple", "banana", "cherry"})  # frozenset
    i = None                                      # NoneType
    '''


    # ==================== NUMERIC TYPES ====================
    
    # INT (Integer):
    # Unlike Java (int: -2^31 to 2^31-1, long: -2^63 to 2^63-1),
    # Python's int has NO size limit! It can be infinitely large.
    '''
    x = 1
    y = 35656222554887711
    z = -3255522

    print(type(x))  # Output: <class 'int'>
    '''

    # FLOAT (Floating Point):
    # Contains one or more decimals
    # Can also be scientific notation with 'e' or 'E' to indicate power of 10
    '''
    x = 1.10
    y = 1.0
    z = -35.59

    # Scientific notation examples:
    a = 35e3        # 35 * 10^3 = 35000.0
    b = 12E4        # 12 * 10^4 = 120000.0
    c = -87.7e100   # Very large negative number

    print(a)  # Output: 35000.0
    print(b)  # Output: 120000.0
    '''

    # COMPLEX (Complex Numbers):
    # Written with 'j' as the imaginary part
    # Used for mathematical and scientific computing
    # Cannot be converted to other numeric types
    '''
    x = 3+5j
    y = 5j
    z = -5j

    print(type(x))  # Output: <class 'complex'>
    
    # Accessing real and imaginary parts:
    print(x.real)  # Output: 3.0
    print(x.imag)  # Output: 5.0
    '''

    # Type conversion between numeric types:
    '''
    x = 1      # int
    y = 2.8    # float
    z = 1j     # complex

    # Convert from int to float:
    a = float(x)
    print(a)  # Output: 1.0

    # Convert from float to int (decimal part is removed):
    b = int(y)
    print(b)  # Output: 2

    # Convert from int to complex:
    c = complex(x)
    print(c)  # Output: (1+0j)

    # Note: You CANNOT convert complex to int or float
    '''


    # ==================== RANDOM NUMBERS ====================
    # Python has a built-in 'random' module for generating random numbers
    # Java equivalent: java.util.Random
    
    '''
    import random

    # Generate random integer between 1 and 99 (inclusive)
    print(random.randrange(1, 100))
    
    # Generate random float between 0 and 1
    print(random.random())
    
    # Generate random integer between 1 and 10 (inclusive)
    print(random.randint(1, 10))
    
    # Choose random element from a list
    colors = ["red", "blue", "green"]
    print(random.choice(colors))
    '''


    # ==================== STRINGS ====================

    # Multi-line strings using triple quotes
    # Java equivalent: String text = "line1\nline2\nline3";
    '''
    a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore
et dolore magna aliqua."""
    print(a)
    '''

    # Strings are arrays of characters (immutable)
    # Similar to Java's String class
    '''
    a = "hello world"
    print(a[1])      # Output: e (index starts at 0)
    print(len(a))    # Output: 11 (length of string)
    
    # Iterate through string characters
    for char in a:
        print(char)
    '''

    # Checking if substring exists using 'in' and 'not in'
    # Java equivalent: text.contains("free")
    '''
    txt = "The best things in life are free!"

    print("free" in txt)  # Output: True

    if "free" in txt:
        print("Yes, 'free' is present.")

    if "expensive" not in txt:
        print("No, 'expensive' is NOT present.")
    '''

    # String slicing - extracting parts of a string
    # Syntax: string[start:end:step]
    '''
    b = "Hello, World!"
    
    print(b[2:5])    # Output: llo (characters from index 2 to 4)
    print(b[:5])     # Output: Hello (from start to index 4)
    print(b[7:])     # Output: World! (from index 7 to end)
    print(b[-5:-2])  # Output: orl (negative indexing from end)
    
    # Using step
    print(b[::2])    # Output: Hlo ol! (every 2nd character)
    print(b[::-1])   # Output: !dlroW ,olleH (reverse string)
    '''


    # ==================== STRING METHODS ====================
    
    # upper() and lower() - change case
    '''
    text = "Hello World"
    print(text.upper())  # Output: HELLO WORLD
    print(text.lower())  # Output: hello world
    '''

    # strip() - removes whitespace from beginning and end
    # Java equivalent: text.trim()
    '''
    c = "    hello world    "
    print(c.strip())  # Output: "hello world"
    '''

    # replace() - replaces substring with another string
    # Java equivalent: text.replace("h", "j")
    '''
    e = "hello world"
    print(e.replace("h", "j"))  # Output: jello world
    print(e.replace("world", "python"))  # Output: hello python
    '''

    # split() - splits string into a list
    # Java equivalent: text.split(",")
    '''
    e = "hello, world"
    print(e.split(","))  # Output: ['hello', ' world']
    
    words = "Python is awesome"
    print(words.split())  # Output: ['Python', 'is', 'awesome'] (splits by space)
    '''

    # Other useful string methods:
    '''
    text = "hello world"
    
    print(text.capitalize())    # Output: Hello world
    print(text.title())         # Output: Hello World
    print(text.count("l"))      # Output: 3 (counts occurrences)
    print(text.startswith("h")) # Output: True
    print(text.endswith("d"))   # Output: True
    print(text.find("world"))   # Output: 6 (index of substring)
    '''


    # ==================== STRING FORMATTING ====================
    
    # Method 1: .format() method
    '''
    age = 20
    name = "Berke"
    
    # Using named placeholders
    txt = "My name is {name} and I'm {age} years old"
    print(txt.format(name=name, age=age))
    
    # Using positional placeholders
    txt = "My name is {} and I'm {} years old"
    print(txt.format(name, age))
    
    # Formatting numbers
    txt = "I am {age:.2f} years old"
    print(txt.format(age=age))  # Output: I am 20.00 years old
    '''

    # Method 2: f-strings (Python 3.6+) - RECOMMENDED
    # Cleaner and more readable than .format()
    '''
    age = 20
    name = "Berke"
    
    txt = f"My name is {name} and I'm {age} years old"
    print(txt)
    
    # Expressions inside f-strings
    print(f"Next year I'll be {age + 1}")
    print(f"My name in uppercase: {name.upper()}")
    
    # Formatting numbers
    price = 59.75432
    print(f"Price: ${price:.2f}")  # Output: Price: $59.75
    '''


    # ==================== BOOLEAN TYPE ====================
    # Python's bool type: True or False (note the capital T and F)
    # Java: boolean (true/false with lowercase)
    
    '''
    is_student = True
    is_working = False
    
    print(type(is_student))  # Output: <class 'bool'>
    '''

    # bool() function - converts values to boolean
    # Most values are True, but some are False:
    # - Empty collections: [], {}, (), ""
    # - Zero: 0, 0.0
    # - None
    '''
    # These return True:
    print(bool("hello"))       # Output: True (non-empty string)
    print(bool(123))           # Output: True (non-zero number)
    print(bool(["apple"]))     # Output: True (non-empty list)
    
    # These return False:
    print(bool(""))            # Output: False (empty string)
    print(bool(0))             # Output: False (zero)
    print(bool([]))            # Output: False (empty list)
    print(bool({}))            # Output: False (empty dictionary)
    print(bool(()))            # Output: False (empty tuple)
    print(bool(None))          # Output: False (None)
    '''

    # Practical use of bool():
    '''
    def check_list(my_list):
        if bool(my_list):  # or simply: if my_list:
            print("List has items")
        else:
            print("List is empty")
    
    check_list([1, 2, 3])  # Output: List has items
    check_list([])         # Output: List is empty
    '''

    # Comparison and logical operations return boolean:
    '''
    print(10 > 9)              # Output: True
    print(10 == 9)             # Output: False
    print(10 < 9)              # Output: False
    
    x = 10
    y = 5
    print(x > 5 and y < 10)    # Output: True
    print(x > 15 or y < 10)    # Output: True
    print(not(x > 15))         # Output: True
    '''
