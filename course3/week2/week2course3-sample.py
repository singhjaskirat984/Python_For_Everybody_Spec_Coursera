import re
handle = open('sampleData.txt')
lst = list()
inp = handle.read()
lst = re.findall('[0-9]+',inp)
numlist = list()
for Astring in  lst:
	num = int(Astring)
	numlist.append(num)
print(sum(numlist))
