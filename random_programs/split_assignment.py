fname = input("enter file name: ")
fh = open(fname)
word = ""
lst = list()
for line in fh:
	line=line.rstrip()
	if lst == []:
		lst = line.split()
	else:
		lst2 = line.split()
		for word in lst2 :
			 if word in lst:
			 	continue
			 lst.append(word)
lst.sort()
print(lst)




# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#     line = line.rstrip()
#     if lst==[] : 
#         lst = line.split()
        
#     else :
#         for word in lst:
#             if word in line :
#                 continue
#             lst.append(word)    
# lst.sort()        
# print(lst)
