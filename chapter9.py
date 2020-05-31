#simplified counting with get

counts = dict()
names = ['abc' ,'efg', 'xyz', 'pqr']
for name in names:
	counts[name] =counts.get(name,0)+1
print(counts)