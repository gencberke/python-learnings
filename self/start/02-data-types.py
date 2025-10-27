import sys
import random

if __name__ == '__main__':
    print(sys.version)

    #========= Built-in Data Types ===========

    # Text -> str (string)
    # Numeric -> int, float, complex
    # Sequence Types -> list, tuple, range
    # Mapping Type -> dict
    # Set Types -> set, frozenset
    # Boolean Type -> bool
    # Binary Types -> bytes, bytearray, memoryview
    # None Type -> NoneType

    # Some examples of setting them
    """
    a = 20.5
    b = 1j
    c = ["apple", "banana", "cherry"] # list
    d = ("a", "b", "c") # tuple
    e = range(6) # range
    f = {"name": "John", "age": 18} # dict
    g = {"apple", "banana", "cherry"} # set
    h = frozenset({"apple", "banana", "cherry"}) # frozenset
    i = None # NoneType
    """

    # Numerics
    # Int: integer has no borders in python. its unlimited

    # Float: containing one or more decimal float can also be scientific numbers with an "e" to indicate the power of 10
    """
    x = 35e3
    y = 12E4
    z = -87.7e100
    """

    # Complex: complex numbers are written with a "j" as the imaginary part and they can't convert to other numerics
    """
    x = 3+5j
    y = 5j
    """

    # we have a python module to create random numbers called 'random'
    """
    print(random.randrange(1, 100))
    """

    # String

    # multiline string
    a = """lorem ipsum dolor sit amet,
consectetur adipiscing elit.
sed do eiusmod tempor incididunt voluptate."""
    print(a)

    # String is an array like many other languages in python
    a = "hello world"
    print(a[1])
    print(len(a))

    # we can look for containing keyword with 'in' and 'not in' keyword:
    txt = "the best things in life are free!"

    print("free" in txt)
    if "free" in txt:
        print("free")
    if "car" not in txt:
        print("the txt not contains 'car'")

    # you can return a range of characters and negative indexes to start from end
    b = "hello world"
    print(b[2:5])
    print(b[:5])
    print(b[5:])

    print(b[-5:-2])

    # the upper() method and the lower() method return the string in upper and lower characters
    # strip method removes any whitespace from the beginning or the end
    c = "    hello world"
    print(c.strip())

    # replace() method replaces a string with another string
    e = "hello world"
    print(e.replace("h", "j"))

    # split() method returns a list where the text between the specified separator becomes the list items
    e = "hello, world"
    print(e.split(","))

    # .format() string format is included in python with python 3.6
    age = 20
    txt = "My name is berke and I'm {age} years old"
    print(txt.format(age=age))
    txt = "I am {age:.2f} years old"
    print(txt.format(age=age))

    # boolean
    # bool metodu true false döndürmede çok işlevsel mesela string boş stringse tuple list boşlarsa veya sayı 0 ise
    # false döndürüyor
    print(bool("hello world"))
