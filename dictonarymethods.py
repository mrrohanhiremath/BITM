# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Using built-in methods
print("Keys:", my_dict.keys())     # Output: Keys: dict_keys(['a', 'b', 'c'])
print("Values:", my_dict.values()) # Output: Values: dict_values([1, 2, 3])
print("Items:", my_dict.items())   # Output: Items: dict_items([('a', 1), ('b', 2), ('c', 3)])

print("Value for key 'a':", my_dict.get('a'))  # Output: Value for key 'a': 1
print("Value for key 'd':", my_dict.get('d', 'Key not found'))  # Output: Value for key 'd': Key not found

my_dict.update({'d': 4})  # Adding a new key-value pair
print("Updated Dictionary:", my_dict)  # Output: Updated Dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print("Removed item:", my_dict.pop('a'))  # Output: Removed item: 1
print("Dictionary after popping 'a':", my_dict)  # Output: Dictionary after popping 'a': {'b': 2, 'c': 3, 'd': 4}

print("Popped item:", my_dict.popitem())  # Output: Popped item: ('d', 4)
print("Dictionary after popping an item:", my_dict)  # Output: Dictionary after popping an item: {'b': 2, 'c': 3}

my_dict.clear()  # Clearing the dictionary
print("Cleared Dictionary:", my_dict)  # Output: Cleared Dictionary: {}