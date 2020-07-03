hrs = input("Enter Hours:")
rate = input("enter Rate:")
h = float(hrs)
r =float(rate)

if(h<40):
    answer = h*r
    print(answer)
    
else:
    answer1 = 40*r
    hoursAbove40 = h-40
    newRate = r*1.5
    answer2 = hoursAbove40*newRate
    totalAnswer = answer1+answer2
    print(totalAnswer)