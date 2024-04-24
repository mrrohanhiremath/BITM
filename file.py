# Open a file in read mode
file_path = "example.txt"
file = open(file_path, "r")

# Read the entire file
content = file.read()
print("File content:")
print(content)

# Close the file
file.close()

# Open the file in write mode
file = open(file_path, "w")

# Write to the file
file.write("This is a new line.")

# Close the file
file.close()s

# Open the file again in read mode
file = open(file_path, "r")

# Read the file to see the changes
updated_content = file.read()
print("Updated file content:")
print(updated_content)

# Close the file
file.close()