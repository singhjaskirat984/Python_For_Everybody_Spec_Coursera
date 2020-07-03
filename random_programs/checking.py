def computepay(hrs,rph):
    hrs=float(hrs)
    rph=float(rph)
    if hrs<=40:
        pay=hrs*rph
    elif hrs>40:
        pay= (40*rph) + ((hrs-40)*1.5*rph)
    else:
        print("error")
    return pay
hrs = input("Enter Hours:")
rph = input("Enter Rate/hr :")
p = computepay(10,20)
print("Pay",p)