import os
print(os.getcwd())
dir = "myDir"
file = "myFile.txt"
if os.path.exists(file):
    os.remove(file)
else:
    print("File not exists")

if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print("Dir exists")
    os.rmdir(dir)

print("Hello Python")
