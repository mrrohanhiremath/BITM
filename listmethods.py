# Create a list
my_list = [1, 2, 3, 4, 5]

# Append an element to the list
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Extend the list with another list
my_list.extend([7, 8, 9])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Insert an element at a specific index
my_list.insert(2, 10)
print(my_list)  # Output: [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]

# Remove an element from the list
my_list.remove(5)
print(my_list)  # Output: [1, 2, 10, 3, 4, 6, 7, 8, 9]

# Pop an element from the list (default is the last element)
popped_element = my_list.pop()
print(popped_element)  # Output: 9
print(my_list)  # Output: [1, 2, 10, 3, 4, 6, 7, 8]

# Find the index of an element in the list
index = my_list.index(3)
print(index)  # Output: 3

# Count occurrences of an element in the list
count = my_list.count(10)
print(count)  # Output: 1

# Sort the list
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4, 6, 7, 8, 10]

# Reverse the list
my_list.reverse()
print(my_list)  # Output: [10, 8, 7, 6, 4, 3, 2, 1]

# Clear the list
my_list.clear()
print(my_list)  # Output: []