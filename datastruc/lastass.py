count = 0
total = 0

while True:
    x=input('Enter number')
    if x=='done':
        break
    else:
        try:
             x = int(x)
        except:
            print('enter only numbers or done')
            continue

    count = count+1
    total = total+x


print(count,total,count/total)
