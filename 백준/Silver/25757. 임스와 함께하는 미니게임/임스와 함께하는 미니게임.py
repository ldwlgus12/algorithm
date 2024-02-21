import sys
n, g = sys.stdin.readline().split()
name = [sys.stdin.readline() for _ in range(int(n))]
name = list(set(name))

if g == 'Y':	
    print(len(name))
elif g == 'F':
    print(len(name) // 2)
elif g == 'O':
    print(len(name) // 3)
    