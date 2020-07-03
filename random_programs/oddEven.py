n = input('enter no.')
num = int(n)
oddEven = num%2
if oddEven != 0 :
    print('weird')

else:
    if num>=2 and num<=5:
        print('not weird')
    elif num>=6 and num<=20:
        print('weird')
    elif num>20:
        print('not weird')