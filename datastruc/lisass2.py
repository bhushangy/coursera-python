fhand = open('words.txt')
count = 0
for line in fhand:
    if line.startswith('From ') :  # see there are lines with 'From:' and 'From '
        l = line.split()
        print(l[1])
        count = count+1


print('There were',count,'lines in the file with From as the first word')
