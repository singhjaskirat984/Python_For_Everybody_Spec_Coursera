name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
lst = list()
for line in handle :
	if not line.startswith('From '):continue
	words = line.split()
	address = words[1]
	lst.append(address)
	
for email in lst :
	counts[email] = counts.get(email,0)+1

# or

# for email in lst:
# 	if email not in counts:
# 		counts[email] = 1
# 	else:
# 		counts[email] = counts[email] + 1

bigCount = None
bigWord = None
for word,count in counts.items():
	if bigCount is None or count > bigCount:
		bigWord = word
		bigCount = count

print(bigWord,bigCount)