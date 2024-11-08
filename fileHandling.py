import os


# open file
# f = open('stringPy.py' , 'rt')

# print(f.read())

# print(f.readlines())

# for x in f:
#   print(x)

# print(f.read())
# f.close()


# ///// removing file ////////
# os.remove('myFile.txt')

if os.path.exists('myFile.txt'):
    f = open('myFile.txt' , 'a')
    f.write("\nFile already exists")
    f.close()
else:
    f = open('myFile.txt' , 'x')
    f.write("This file is create with python")
    f.close()

f = open('myFile.txt')
print(f.read())
