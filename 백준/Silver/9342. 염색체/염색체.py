import re
t = int(input())
a = re.compile('^[A-F]?A+F+C+[A-F]?$')

for i in range(t):
	string = input()
    
	if a.match(string) == None:
		print('Good')
	else:
		print('Infected!')
        