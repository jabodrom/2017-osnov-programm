f = open('suffixes.txt','r',encoding='utf-8-sig')
ends = []
for x in f.readlines():
    ends.append(x.strip())
f.close()
ends = sorted(ends,key=lambda x: len(x),reverse=True)

f = open('prefixes.txt','r',encoding='utf-8-sig')
starts = []
for x in f.readlines():
    starts.append(x.strip())
f.close()
starts = sorted(starts,key=lambda x: len(x),reverse=True)

f = open('circumfixes.txt','r',encoding='utf-8')
circ = []
for x in f.readlines():
    circ.append(x.strip().split('\t'))
f.close()

f = open('stems.txt','r',encoding='utf-8-sig')
stems = set()
for line in f.readlines():
    stems.add(line.strip())
f.close()

def find_stem(word):
    for c in circ:
        if word.startswith(c[0]) and word.endswith(c[1]):
            word = word[len(c[0]):-len(c[1])]
            break
    cut = True
    while cut:
        cut = False
        for start in starts:
            if word.startswith(start):
                word = word[len(start):]
                cut = True
                break
    cut = True
    while cut:
        cut = False
        for end in ends:
            if word.endswith(end):
                word = word[:-len(end)]
                cut = True
                break
    word = word.strip('ы')
    if word and word in stems:
        in_dict = True
    else:
        in_dict = False
    return word, in_dict


c = []
f = open('ckt_tagged.txt','r',encoding='utf-8')
fw = open('ckt_stemmed.tsv','w',encoding='utf-8')
for line in f.readlines():
    if line.startswith('#') or line.strip() == '':
        fw.write(line)
    else:
        spl = line.split('\t')
        word = spl[1].strip()
        stem,certain = find_stem(word.lower())
        c.append(certain)
        fw.write(word+'\t'+stem+'\t'+str(certain)+'\n')
fw.close()

print(len(c),sum(c),sum(c)/len(c))
