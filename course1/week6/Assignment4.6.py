def computepay(h,r):
    if h<40 : 
        totalAnswer = h*r
        
    elif h>40 :
        ansUpto40 = 40*r
        hrsAbove40 = h-40
        rateAbove40 = r*1.5
        answerAbove40 = hrsAbove40 * rateAbove40
        totalAnswer = ansUpto40 + answerAbove40
        
    return totalAnswer

hrs = input("Enter Hours:")
rate = input("Enter rate:")
floatHrs = float(hrs)
floatRate = float(rate)

p = computepay(floatHrs,floatRate)

print("Pay",p)