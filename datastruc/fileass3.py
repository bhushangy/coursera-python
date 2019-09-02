x = input('enter filename')
fhand = open(x)
count = 0
tot = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:') :
       count = count+1
       pos1 = line.find(' ')
       val = float(line[pos1+1:]) #here u need not print out the resulting substring from the slice operation 
       tot = tot+val


print('Average spam confidence: ',(tot/count))
