# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
x = fh.read()
y = x.upper()
z = y.rstrip()
print(z)