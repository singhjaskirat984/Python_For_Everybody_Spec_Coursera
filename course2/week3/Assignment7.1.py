# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read()
inp = inp.rstrip()
answer = inp.upper()
print(answer)
