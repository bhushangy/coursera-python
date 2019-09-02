x = input('enter filename')
fhand = open(x)
for line in fhand:
    print(line.upper())
