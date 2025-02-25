import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]
dic = {}

for i in words: 
    x = len(i)-1
    for j in i:
        if j in dic:
            dic[j] += 10**x
        else:
            dic[j] = 10**x
        x -= 1

dic_sort = sorted(dic.values(), reverse=True)
result = 0
num = 9

for i in dic_sort:
    result += i * num
    num -= 1
    
print(result)
