small = None
large = None

while True:
    x=input()
    if x=='done':
        break
    else:
        try:
             x = int(x)
        except:
            print('Invalid input')
            continue

    if small==None:
        small=x
    if x<small:
        small =x

    if large==None:
        large=x
    if x>large:
        large=x


print('Maximum is',large)
print('Minimum is',small)
