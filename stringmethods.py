# Define a sample string
sample_string = "   Hello, World!   "

# Convert to uppercase
uppercase_string = sample_string.upper()
print("Uppercase:", uppercase_string)

# Convert to lowercase
lowercase_string = sample_string.lower()
print("Lowercase:", lowercase_string)

# Capitalize the string
capitalized_string = sample_string.capitalize()
print("Capitalized:", capitalized_string)

# Title case the string
title_case_string = sample_string.title()
print("Title Case:", title_case_string)

# Strip leading and trailing whitespace
stripped_string = sample_string.strip()
print("Stripped:", stripped_string)

# Replace occurrences of a substring
replaced_string = sample_string.replace("Hello", "Hi")
print("Replaced:", replaced_string)

# Split the string
split_string = sample_string.split(",")
print("Split:", split_string)

# Join the elements of a list into a string
list_of_words = ["Hello", "World", "!"]
joined_string = " ".join(list_of_words)
print("Joined:", joined_string)