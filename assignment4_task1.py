try:
    f = open('sample.txt','r')
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
else:
    print("Reading file content:")
    print("Line 1: ",f.readline(),end = "")
    print("Line 2: ",f.readline())