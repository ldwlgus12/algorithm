import sys
input = sys.stdin.readline

n = int(input())
s = input()

color = {'B': 0, 'R': 0} 
color[s[0]] += 1 

for i in range(1, n): 
    if s[i] != s[i-1]:
        color[s[i]] += 1

result = min(color['B'], color['R']) + 1

print(result)
