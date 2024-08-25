
file = open('D:/DEFT Intern/Nafis Tahmid/Python/Files/test_file.txt', 'r')

# This will print every line one by one in the file
for each in file:
    print(each)

# Extract all strings
print(file.read())

# With with method
with open('D:/DEFT Intern/Nafis Tahmid/Python/Files/test_file.txt') as file:
    data = file.read()
print(data)
# Print the first 5 characters
print(file.read(7))

# Split files
with open('D:/DEFT Intern/Nafis Tahmid/Python/Files/test_file.txt') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

# Write functions
file = open('D:/DEFT Intern/Nafis Tahmid/Python/Files/test_file.txt', 'w')
file.write("This is the write test command")
file.close()
Now reading the file
file = open('D:/DEFT Intern/Nafis Tahmid/Python/Files/test_file.txt', 'r')
print(file.read())
with along with write
with open('D:/DEFT Intern/Nafis Tahmid/Python/Files/test_file.txt', 'w') as file:
    file.write("Testing hello world!!!")
    file.write("Testing hello world again!!!")
    file.write("Testing hello world again and again!!!")
    file.close()

# Print the same file
file = open('D:/DEFT Intern/Nafis Tahmid/Python/Files/test_file.txt', 'r')
print(file.read())
# Using the append mode -> allows to add a new line
file = open('D:/DEFT Intern/Nafis Tahmid/Python/Files/test_file.txt', 'a')
file.write("Adding a new line to the same file")
file.close()
# Printing the same file again
file = open('D:/DEFT Intern/Nafis Tahmid/Python/Files/test_file.txt', 'r')
print(file.read())