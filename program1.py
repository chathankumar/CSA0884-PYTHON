# Write to a file
with open('example.txt', 'w') as file:
    file.write("Hello, World!\nThis is a text file example.\n")

# Read from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print("File content:")
    print(content)

# Update the file
with open('example.txt', 'a') as file:
    file.write("Appending new content to the file.\n")

# Read the updated file
with open('example.txt', 'r') as file:
    updated_content = file.read()
    print("\nUpdated file content:")
    print(updated_content)
