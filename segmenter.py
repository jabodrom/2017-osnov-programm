import sys

text = sys.stdin.read()

text = text.replace('. ',  '.\n')
text = text.replace('с.\nш.\n', 'с. ш. ' )
text = text.replace('з.\nд.\n', 'з. д. ' )

print(text)