#the top 10 most common words

fhand = open('filename.txt')
counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0)+1
lst = list()
for key,value in counts.item():
	newtup = (value,key)
	last.append(newtup)
lst = sorted(lst, reverse=True)

for value,key in lst[:10]:
	print(key,value)