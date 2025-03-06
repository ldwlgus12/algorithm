import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for i in range(n):
    nums = int(input())
    if nums in dic:
        dic[nums] += 1
    else:
        dic[nums] = 1

result = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])
