counts = dict()
name = ['csev' ,'cwen' , 'csev' , 'cwen' , 'zqian']

for word in  name:
     # if word not in counts:
     counts[word] = counts.get(word , 0) + 1
     # else:
     #      counts[word] = counts[word]  + 1

print(counts)