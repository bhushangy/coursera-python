def comp(h,r):
    if hrs>40 :
        return ((h-40)*1.5*r)+(40*r)
    else:
        return (h*r)





hrs = float(input("Enter Hours:"))
rph = float(input("Enter rate per hour:"))
print(comp(hrs,rph))
