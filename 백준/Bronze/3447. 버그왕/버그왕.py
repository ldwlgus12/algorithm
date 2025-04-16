import sys
input = sys.stdin.readlines
code = input()

for i in code:
    i = i.rstrip()

    while 'BUG' in i:
        i = i.replace('BUG', '')    
    print(i)
    