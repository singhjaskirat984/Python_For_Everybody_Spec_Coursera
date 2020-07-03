score = input("Enter Score: ")

try:
    floatScore = float(score)
    
except:
    print('enter valid score')
    quit()
    
if(floatScore < 0.0 or floatScore > 0.9):
    print('enter score b/w 0.0 and 0.9')
    
elif(floatScore>= 0.9):
    print('A')
    
elif(floatScore>=0.8):
    print('B')
    
elif(floatScore>=0.7):
    print('C')

elif(floatScore>=0.6):
    print('D')
    
else: 
    print('F')