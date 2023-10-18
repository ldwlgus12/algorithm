import sys
n, m = map(int, input().split())
dict = {}

for i in range(n):
    word = sys.stdin.readline().strip()
    
    if len(word) >= m:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
            
dict = sorted(dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for j in dict:
    print(j[0])