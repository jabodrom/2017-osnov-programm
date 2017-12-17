m = []
f = open('ckt_map.txt','r',encoding='utf-8-sig')
for line in f.readlines():
    m.append(line.strip().split('\t'))
f.close()

f = open('ckt_tok.txt','r',encoding='utf-8')
fw = open('ckt_tok_trans.txt','w',encoding='utf-8')
for line in f.readlines():
    if line.startswith('#'):
        fw.write(line)
    else:
        word = line.split('\t')[1].strip()
        for el in m:
            word = word.replace(el[0],el[1])
        fw.write(line.strip()+'\t'+'Translit='+word+'\n')
