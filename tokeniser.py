import sys

text = sys.stdin.readlines()

sent_id = 1
tokenized = ''

for line in text:
	line = line.strip()
	if line == '':
		continue
	line = line.replace('\t',  ' ')
	tokenized += '# sent_id = ' + str(sent_id) + '\n'
	tokenized += '# text = ' + line + '\n'
	line = line.replace(':',  ' :')
	line = line.replace(',',  ' ,')
	line = line.replace('.',  ' .')
	line = line.replace('(',  '( ')
	line = line.replace(')',  ' )')
	line = line.replace('?',  ' ?')
	line = line.replace('!',  ' !')
	line = line.replace(';',  ' ;')
	line = line.replace(' \"',  ' \" ')
	line = line.replace('\" ',  ' \" ')
	sent_id = sent_id + 1
	
	token_id = 1
	tokens = line.split(' ')
	for token in tokens:
		if token == '':
			continue
		tokenized += str(token_id) + '\t' + token + '\t_\t_\t_\t_\t_\t_\t_\t_\n'
		token_id = token_id + 1
print(tokenized)
