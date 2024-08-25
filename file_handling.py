import os

def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write("Hello world\n")
        print("File " + filename + " created successfully!")
    except IOError:
        print("Error: could not create file " + filename)

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: could not read file " + filename)

def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        print("Text appended to file " + filename + "successfully")
    except IOError:
        print("Error: could not append file " + filename)

def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print("File " + filename + " renamed to " + new_filename + " successfully.")
    except IOError:
        print("Error: could not rename file " + filename)

def removefile(filename):
    try:
        os.remove(filename)
        print("File name " + filename + " removed successfully")
    except IOError:
        print("Error: could not remove file " + filename)

if __name__ == '__main__':
    filename = "example.txt"
    new_filename = "new_example.txt"
    text= "Trying appending"
    # create_file(filename)
    # read_file(filename)
    # append_file(filename, text)
    # read_file(filename)
    # rename_file(filename, new_filename)
    # removefile(filename)
 
    # Python tell
    # Open a file
    file = open('D:/DEFT Intern/Nafis Tahmid/Python/Files/test_file.txt', 'r')
    # Read the file
    print(file.read(13))
    # Check the current position
    pointer = file.tell()
    # print("Current position:", pointer)
    # Close the file
    file.close()
