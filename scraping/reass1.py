import re
fhand = open('romeo.txt')
l = list()
v = list()
for line in fhand:
    line = line.rstrip()
    v = re.findall('[0-9]+',line)
    for i in v:
        l.append(int(i))

print(sum(l))
