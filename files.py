import sys
i = 0
for linea in sys.stdin: 
	if len(linea.strip())!=0:
		i +=1
		linea=linea.rstrip('\n')

print (i)
