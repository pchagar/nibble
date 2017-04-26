import itertools

i = 2
d = {}
with open("countSeqTest1.txt") as fin, open('output.csv', 'wb') as fout:
	#read every 4th line starting at the 2nd line
	for line in itertools.islice(fin, 1, None, 4):
		#strip newlines
		key = line.strip()
		#if the key is already in the dict increment the counter
		if key in d:
			d[key] = d[key] + 1
		else:
        			d[key] = 1
	for k,v in d.items():
		fout.write(str(k))
		fout.write(", ")
		fout.write(str(v))
		fout.write("\n")