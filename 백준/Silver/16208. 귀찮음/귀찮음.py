import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
s_lst = sum(lst)
result = 0

for i in lst:
    result += i * (s_lst - i)
    s_lst -= i
    
print(result)