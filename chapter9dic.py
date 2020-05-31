#getting the file words into dictionaries
#then find which word is comes the most in the dictionaries
#print the count and the word in file

name = input('enter file')
handle = open(name)

counts = dict()
for line in handle:
	words = line.split()
	for word in words:
		counts[word] = counts(word,0)+1
#now code for finding big count
bigcount = None
bigword = None
for word,count in counts.item():
	if bigcount is None or count>bigcount:
		bigword = word
		bigcount = count
		
print(bigword,bigcount)