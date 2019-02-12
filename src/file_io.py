"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
import os
import sys

def build_path(file_name):
    return os.path.join(sys.path[0], file_name)

with open(build_path("foo.txt"), "r") as foo:
    text = foo.read()
    print(text)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open(build_path("bar.txt"), "w") as bar:
    bar.write("The drought had lasted now for ten million years, and the reign of the terrible lizards had long since ended.\nHere on the Equator, in the continent which would one day be known as Africa, the battle for existence had reached a new climax of ferocity, and the victor was not yet in sight.\nIn this barren and desiccated land, only the small or the swift or the fierce could flourish, or even hope to survive.")
