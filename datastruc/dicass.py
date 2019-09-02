fhand = open('words.txt')
l = list()
s = list()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        l = line.split()
        s.append(l[1])

dd = dict()
for name in s:
    dd[name] = dd.get(name,0) + 1


t = dd.items()
bigc = None
bigw = None
for key,count in t:
    if bigw is None or count>bigc :
        bigc = count
        bigw = key

print(bigw,(bigc))
