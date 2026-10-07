# python file detection

# os = operating system --> provides a way for python programs to interact with the operating system
# relative file path = stuff/test.txt --- absolute file path = C:\Users\BEHNAM\OneDrive\Desktop\test.txt
# \\ = /

import os

file_path = "C:\\Users\\BEHNAM\\OneDrive\\Desktop\\test"

if os.path.exists(file_path):
    print(f"the location {file_path} exists")

    if os.path.isfile(file_path):
        print("its a file")
    elif os.path.isdir(file_path):
        print("its a directory")
else:
    print("that location does not exist")