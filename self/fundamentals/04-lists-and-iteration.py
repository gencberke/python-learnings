if __name__ == "__main__":

    # ==================== PYTHON LISTS ====================
    # Lists are mutable (can be changed) and allow duplicate values
    # Java equivalent: ArrayList<Object>
    
    # Key characteristics:
    # - Ordered: Items have a defined order that won't change
    # - Changeable: Can add, remove, or modify items after creation
    # - Allow duplicates: Can have items with the same value
    # - Dynamic size: Size can grow or shrink (unlike Java arrays)
    
    '''
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, "apple", "banana"]
    print(mylist)
    '''

    # Lists can contain mixed data types (not recommended but possible)
    '''
    mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
    print(mixed_list)
    '''


    # ==================== LIST BASICS ====================
    
    # Getting length with len() function
    # Java equivalent: list.size()
    '''
    mylist = [1, 2, 3, 4, 5]
    print(len(mylist))  # Output: 5
    '''

    # type() function shows it's a list class
    '''
    mylist = [1, 2, 3]
    print(type(mylist))  # Output: <class 'list'>
    '''

    # List constructor - creating a list with list()
    # Java equivalent: new ArrayList<>(Arrays.asList(...))
    '''
    this_list = list(("apple", "banana", "cherry"))
    print(this_list)  # Output: ['apple', 'banana', 'cherry']
    '''


    # ==================== ACCESSING LIST ELEMENTS ====================
    
    # Indexing (starts at 0, just like Java)
    '''
    fruits = ["apple", "banana", "cherry"]
    print(fruits[0])   # Output: apple
    print(fruits[1])   # Output: banana
    print(fruits[-1])  # Output: cherry (negative index from end)
    print(fruits[-2])  # Output: banana
    '''

    # Slicing - extracting a range of elements
    # Syntax: list[start:end:step]
    '''
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print(mylist[5:11])   # Output: [6, 7, 8, 9, 10] (from index 5 to 10)
    print(mylist[:5])     # Output: [1, 2, 3, 4, 5] (from start to index 4)
    print(mylist[5:])     # Output: [6, 7, 8, 9, 10] (from index 5 to end)
    print(mylist[::2])    # Output: [1, 3, 5, 7, 9] (every 2nd element)
    print(mylist[::-1])   # Output: [10, 9, 8, ..., 1] (reverse list)
    '''

    # Checking if item exists using 'in' operator
    # Java equivalent: list.contains()
    '''
    mylist = [1, 2, 3, "apple", "banana"]
    
    if "banana" in mylist:
        print("Found banana!")
    
    if 10 not in mylist:
        print("10 is not in the list")
    '''


    # ==================== MODIFYING LISTS ====================
    
    # Changing single item
    '''
    fruits = ["apple", "banana", "cherry"]
    fruits[1] = "strawberry"
    print(fruits)  # Output: ['apple', 'strawberry', 'cherry']
    '''

    # Changing multiple items using slicing
    '''
    fruits = ["apple", "banana", "cherry"]
    fruits[1:3] = ["grapes", "melon"]
    print(fruits)  # Output: ['apple', 'grapes', 'melon']
    '''

    # Insert at specific position with insert()
    # Java equivalent: list.add(index, element)
    '''
    fruits = ["apple", "banana", "cherry"]
    fruits.insert(1, "watermelon")
    print(fruits)  # Output: ['apple', 'watermelon', 'banana', 'cherry']
    '''


    # ==================== ADDING ELEMENTS ====================
    
    # append() - add single item to the end
    # Java equivalent: list.add(element)
    '''
    fruits = ["apple", "banana", "cherry"]
    fruits.append("grapes")
    print(fruits)  # Output: ['apple', 'banana', 'cherry', 'grapes']
    '''

    # extend() - add multiple items from another iterable
    # Java equivalent: list.addAll()
    '''
    fruits = ["apple", "banana", "cherry"]
    tropical = ["mango", "pineapple", "papaya"]
    
    fruits.extend(tropical)
    print(fruits)  # Output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
    
    # Can also extend with other iterables
    fruits.extend(["grapes", "melon"])
    print(fruits)
    '''

    # Difference between append() and extend():
    '''
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    
    list1.append([4, 5])
    print(list1)  # Output: [1, 2, 3, [4, 5]] (adds list as single element)
    
    list2.extend([4, 5])
    print(list2)  # Output: [1, 2, 3, 4, 5] (adds each element separately)
    '''


    # ==================== REMOVING ELEMENTS ====================
    
    # remove() - removes specific value (first occurrence)
    # Java equivalent: list.remove(Object)
    '''
    fruits = ["apple", "banana", "cherry", "banana"]
    fruits.remove("banana")
    print(fruits)  # Output: ['apple', 'cherry', 'banana'] (only first banana removed)
    '''

    # pop() - removes item at specific index and returns it
    # Java equivalent: list.remove(index)
    '''
    fruits = ["apple", "banana", "cherry"]
    removed_item = fruits.pop(1)
    print(removed_item)  # Output: banana
    print(fruits)        # Output: ['apple', 'cherry']
    
    # pop() without index removes last item
    last_item = fruits.pop()
    print(last_item)  # Output: cherry
    '''

    # del keyword - removes item at specific index or entire list
    '''
    fruits = ["apple", "banana", "cherry"]
    del fruits[0]
    print(fruits)  # Output: ['banana', 'cherry']
    
    # Delete entire list
    # del fruits  # This would delete the entire list variable
    '''

    # clear() - removes all items but keeps the list
    # Java equivalent: list.clear()
    '''
    fruits = ["apple", "banana", "cherry"]
    fruits.clear()
    print(fruits)  # Output: []
    '''


    # ==================== LOOPING THROUGH LISTS ====================
    
    # Method 1: For-each loop (most common)
    # Java: for (String fruit : fruits) { ... }
    '''
    fruits = ["apple", "banana", "cherry"]
    
    for fruit in fruits:
        print(fruit)
    '''

    # Method 2: Using range and len (when you need index)
    # Java: for (int i = 0; i < fruits.size(); i++) { ... }
    '''
    fruits = ["apple", "banana", "cherry"]
    
    for i in range(len(fruits)):
        print(f"{i}: {fruits[i]}")
    '''

    # Method 3: Using enumerate() (best when you need both index and value)
    # This is cleaner than using range(len())
    '''
    fruits = ["apple", "banana", "cherry"]
    
    for i, fruit in enumerate(fruits):
        print(f"{i}: {fruit}")
    
    # Can start counting from different number
    for i, fruit in enumerate(fruits, start=1):
        print(f"{i}: {fruit}")  # Starts from 1 instead of 0
    '''

    # Method 4: While loop
    '''
    fruits = ["apple", "banana", "cherry"]
    i = 0
    
    while i < len(fruits):
        print(fruits[i])
        i += 1
    '''


    # ==================== LIST COMPREHENSION ====================
    # Concise way to create lists based on existing lists
    # Java doesn't have direct equivalent (need Stream API)
    
    # Basic syntax: [expression for item in iterable if condition]
    
    # Example 1: Filter items containing 'a'
    '''
    fruits = ["apple", "banana", "cherry", "kiwi"]
    new_list = [fruit for fruit in fruits if "a" in fruit]
    print(new_list)  # Output: ['apple', 'banana']
    '''

    # Example 2: Square of numbers
    '''
    values = [1, 2, 3, 5, 7, 9]
    squares = [value * value for value in values]
    print(squares)  # Output: [1, 4, 9, 25, 49, 81]
    '''

    # Example 3: Conditional expression in list comprehension
    '''
    values = [1, 2, 3, 5, 7, 9]
    even_or_odd = ["even" if value % 2 == 0 else "odd" for value in values]
    print(even_or_odd)  # Output: ['odd', 'even', 'odd', 'odd', 'odd', 'odd']
    '''

    # Example 4: Transform strings
    '''
    names = ["john", "mary", "bob"]
    capitalized = [name.upper() for name in names]
    print(capitalized)  # Output: ['JOHN', 'MARY', 'BOB']
    '''

    # Example 5: Nested list comprehension
    '''
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''

    # Java equivalent using Stream API (Java 8+):
    # List<Integer> squares = values.stream()
    #     .map(v -> v * v)
    #     .collect(Collectors.toList());


    # ==================== SORTING LISTS ====================
    
    # sort() - sorts the list in place (modifies original list)
    # Java equivalent: Collections.sort(list)
    '''
    numbers = [5, 2, 8, 1, 9]
    numbers.sort()
    print(numbers)  # Output: [1, 2, 5, 8, 9]
    
    # Reverse order
    numbers.sort(reverse=True)
    print(numbers)  # Output: [9, 8, 5, 2, 1]
    '''

    # Sorting strings (alphabetically)
    '''
    fruits = ["banana", "apple", "cherry", "date"]
    fruits.sort()
    print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']
    '''

    # Custom sorting with key parameter
    '''
    # Sort by string length
    fruits = ["apple", "banana", "kiwi", "cherry"]
    fruits.sort(key=len)
    print(fruits)  # Output: ['kiwi', 'apple', 'cherry', 'banana']
    
    # Sort by absolute value
    numbers = [-5, 1, -10, 3]
    numbers.sort(key=abs)
    print(numbers)  # Output: [1, 3, -5, -10]
    '''

    # sorted() - returns new sorted list (doesn't modify original)
    # Java equivalent: Creating new list with sorted stream
    '''
    nums = [3, 1, 4, 2]
    new_list = sorted(nums)
    print(nums)      # Output: [3, 1, 4, 2] (original unchanged)
    print(new_list)  # Output: [1, 2, 3, 4] (new sorted list)
    '''

    # reverse() - reverses the list in place
    '''
    fruits = ["apple", "banana", "cherry"]
    fruits.reverse()
    print(fruits)  # Output: ['cherry', 'banana', 'apple']
    '''


    # ==================== COPYING LISTS ====================
    
    # WRONG: Simple assignment creates reference, not copy
    # Java: Same issue with List<> newList = oldList;
    '''
    fruits = ["apple", "banana", "cherry"]
    newlist = fruits  # This is just a reference copy!
    newlist.append("mango")
    
    print(fruits)   # Output: ['apple', 'banana', 'cherry', 'mango']
    print(newlist)  # Output: ['apple', 'banana', 'cherry', 'mango']
    # Both changed because they point to the same list!
    '''

    # CORRECT: Using copy() method - shallow copy
    # Java equivalent: new ArrayList<>(list)
    '''
    fruits = ["apple", "banana", "cherry"]
    newlist = fruits.copy()
    newlist.append("mango")
    
    print(fruits)   # Output: ['apple', 'banana', 'cherry']
    print(newlist)  # Output: ['apple', 'banana', 'cherry', 'mango']
    '''

    # Alternative: Using list() constructor
    '''
    fruits = ["apple", "banana", "cherry"]
    newlist = list(fruits)
    '''

    # Alternative: Using slicing
    '''
    fruits = ["apple", "banana", "cherry"]
    newlist = fruits[:]
    '''

    # Deep copy - for nested lists
    # Shallow copy doesn't work properly with nested lists
    '''
    import copy
    
    matrix = [[1, 2], [3, 4]]
    
    # Shallow copy (wrong for nested lists)
    shallow = matrix.copy()
    shallow[0][0] = 999
    print(matrix)   # Output: [[999, 2], [3, 4]] - Original changed!
    
    # Deep copy (correct for nested lists)
    matrix = [[1, 2], [3, 4]]
    deep_copy = copy.deepcopy(matrix)
    deep_copy[0][0] = 999
    print(matrix)      # Output: [[1, 2], [3, 4]] - Original unchanged!
    print(deep_copy)   # Output: [[999, 2], [3, 4]]
    '''


    # ==================== OTHER USEFUL LIST METHODS ====================
    
    # count() - returns number of times a value appears
    '''
    fruits = ["apple", "banana", "cherry", "apple"]
    print(fruits.count("apple"))  # Output: 2
    '''

    # index() - returns the index of first occurrence
    # Java equivalent: list.indexOf()
    '''
    fruits = ["apple", "banana", "cherry"]
    print(fruits.index("banana"))  # Output: 1
    
    # If item doesn't exist, raises ValueError
    # print(fruits.index("orange"))  # ValueError!
    '''

    # Using + operator to join lists
    '''
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = list1 + list2
    print(list3)  # Output: [1, 2, 3, 4, 5, 6]
    '''

    # Using * operator to repeat lists
    '''
    list1 = [1, 2]
    list2 = list1 * 3
    print(list2)  # Output: [1, 2, 1, 2, 1, 2]
    '''

    # min(), max(), sum() functions
    '''
    numbers = [5, 2, 8, 1, 9]
    print(min(numbers))  # Output: 1
    print(max(numbers))  # Output: 9
    print(sum(numbers))  # Output: 25
    '''

    # any() and all() functions
    '''
    # any() - returns True if at least one element is True
    print(any([False, False, True]))   # Output: True
    print(any([False, False, False]))  # Output: False
    
    # all() - returns True if all elements are True
    print(all([True, True, True]))     # Output: True
    print(all([True, False, True]))    # Output: False
    '''


    # ==================== LIST AS STACK AND QUEUE ====================
    
    # Stack (LIFO - Last In First Out)
    '''
    stack = []
    stack.append(1)    # Push
    stack.append(2)
    stack.append(3)
    print(stack)       # Output: [1, 2, 3]
    
    item = stack.pop() # Pop
    print(item)        # Output: 3
    print(stack)       # Output: [1, 2]
    '''

    # Queue (FIFO - First In First Out)
    # For better performance, use collections.deque instead
    '''
    from collections import deque
    
    queue = deque()
    queue.append(1)       # Enqueue
    queue.append(2)
    queue.append(3)
    print(queue)          # Output: deque([1, 2, 3])
    
    item = queue.popleft()  # Dequeue
    print(item)           # Output: 1
    print(queue)          # Output: deque([2, 3])
    '''
