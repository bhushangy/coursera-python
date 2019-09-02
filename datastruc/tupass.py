fhand = open('words.txt')

l1 = list()
t = list()
l2 = list()
l3 = list()
l4 = list()

for line in fhand:
    if line.startswith('From '):  # mind the space after From_ cause two types r der...From: and From_
            l1 = line.split()
            t.append(l1[5])

for i in t:
    l2 = i.split(':')
    l3.append(l2[0])

dd = dict()
for i in l3:
    dd[i] = dd.get(i,0)+1


for k,v in dd.items():
    l4.append((k,v))


l4.sort()
for k,v in l4:
        print(k,v)
