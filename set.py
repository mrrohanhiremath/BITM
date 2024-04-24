# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding an element to the set
my_set.add(6)
    
# Removing an element from the set
my_set.remove(3)

# Discarding an element from the set
my_set.discard(7)  # No error raised if element is not present

# Clearing the set
#my_set.clear()

# Pop an arbitrary element from the set
popped_element = my_set.pop()

# Creating another set
another_set = {4, 5, 6, 7, 8}

# Making a shallow copy of the set
copied_set = another_set.copy()

# Updating the set with elements from another set
my_set.update(another_set)

# Finding intersection of sets
intersection_set = my_set.intersection(another_set)

# Finding union of sets
union_set = my_set.union(another_set)

# Finding difference of sets
difference_set = my_set.difference(another_set)

print("Modified Set:", my_set)
print("Popped Element:", popped_element)
print("Copied Set:", copied_set)
print("Intersection Set:", intersection_set)
print("Union Set:", union_set)
print("Difference Set:", difference_set)