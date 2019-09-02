fhand = open('romeo.txt')
inp = fhand.read()
l = inp.split()
print(l)

s = list()
for i in l:
    if i not in s :
        s.append(i)

s.sort()
print(s)
