# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0 
answer = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    count = count + 1
    pos1 = line.find('0')
    value = line[pos1:]
    ans = float(value)
    answer = answer + ans

finalAnswer = answer/count
print("Average spam confidence:", finalAnswer)
