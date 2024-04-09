
from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f): 
    f.seek(1) 

# seek() function is a method used with file objects to change the current file position.
# file_object.seek(offset, whence)
# If whence is 0 (the default), the offset is relative to the beginning of the file.
# If whence is 1, the offset is relative to the current file position.
# If whence is 2, the offset is relative to the end of the file.

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")
current_line = 1

print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file) 

current_line += 1
print_a_line(current_line, current_file) 

current_line += 1
print_a_line(current_line, current_file) 
