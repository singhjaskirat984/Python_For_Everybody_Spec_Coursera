handle = open('paragraph.txt')

str = handle.read()

lst = str.split()

count = 0

for word in lst:
	count = count + 1

print(lst)
print(count)