name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
lst = list()
for line in handle :
	if not line.startswith('From '):continue
	words = line.split()
	time = words[5]
	pieces = time.split(':')
	hrs = pieces[0]
	lst.append(hrs)

for hrs in lst:
	counts[hrs] = counts.get(hrs,0)+1

for k,v in sorted(counts.items()):
	print(k,v)