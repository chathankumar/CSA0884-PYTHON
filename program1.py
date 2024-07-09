with open('example.txt', 'w') as file:
    file.write("Hello, World!\nThis is a text file example.\n")
with open('example.txt', 'r') as file:
    content = file.read()
    print("File content:")
    print(content)
with open('example.txt', 'a') as file:
    file.write("Appending new content to the file.\n")
with open('example.txt', 'r') as file:
    updated_content = file.read()
    print("\nUpdated file content:")
    print(updated_content)
