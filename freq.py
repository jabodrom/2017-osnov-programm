import sys

vocab = {}

for line in sys.stdin.readlines(): 
	if '\t' not in line:
		continue
	row = line.split('\t')
	if len(row) != 10:
		continue
	form = row[1]
	if form not in vocab:
		vocab[form] = 0
	vocab[form] = vocab[form] + 1

freq = []
for w in vocab:
	freq.append((vocab[w], w))
freq.sort(reverse=True)

fd = open('freq.txt', 'w+')
for w in freq:
	fd.write('%d\t%s\n' % (w[0], w[1]))
fd.close()