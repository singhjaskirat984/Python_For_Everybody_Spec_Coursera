text = "X-DSPAM-Confidence:    0.8475";

pos1 = text.find('0')
answer = text[pos1:]
print(float(answer))