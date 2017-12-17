import sys

filename = sys.argv[1]

f = open('ckt_tag.txt','r',encoding='utf-8')
tags = {}
words = {}
for line in f.readlines():
    if not line.startswith('#'):
        spl = line.strip().split('\t')
        word = spl[1].strip()
        tag = spl[3].strip()
        if tag in tags:
            tags[tag] += 1
        else:
            tags[tag] = 1
        if word in words:
            if tag in words[word]:
                words[word][tag] += 1
            else:
                words[word][tag] = 1
        else:
            words[word] = {tag:1}

total_words = len(words)

fw = open(filename,'w',encoding='utf-8')
fw.write('# P\tcount\ttag\tform\n')
for tag in tags:
    fw.write('%f\t%d\t%s\t_\n' % (tags[tag] / total_words,
                                  tags[tag], tag))
for word in words:
    for tag in words[word]:
        fw.write('%f\t%d\t%s\t%s\n' % (words[word][tag] / sum(words[word].values()),
                                       words[word][tag], tag, word))
fw.close()
