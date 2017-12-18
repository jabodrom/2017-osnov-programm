import sys

text = sys.stdin.readlines()
model_name = sys.argv[1]

default_tag = (None,0)
words = {}
m = open(model_name,'r',encoding='utf-8')
for line in m.readlines():
    if line.startswith('#'):
        continue
    spl = line.strip().split()
    tag = (spl[2],float(spl[0]))
    if spl[3] == '_':
        default_tag = max(default_tag,tag,key=lambda x: x[1])
    else:
        if spl[3] in words:
            words[spl[3]] = max(words[spl[3]],tag,key=lambda x: x[1])
        else:
            words[spl[3]] = tag

            
f = open('ckt_tagged.txt','w',encoding='utf-8')
for line in text:
    if line.startswith('#'):
        f.write(line)
    else:
        spl = line.strip().split()
        if spl:
            word = spl[1].strip().lower()
            if word in words:
                tag = words[word][0]
            else:
                tag = default_tag[0]
            spl[3] = tag
            f.write('\t'.join(spl)+'\n')
f.close()
    
