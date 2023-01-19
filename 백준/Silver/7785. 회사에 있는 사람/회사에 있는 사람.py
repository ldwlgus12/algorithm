N = int(input())
dic = {}

for i in range(N):
    name, log = input().split()

    if log == 'enter':
        dic[name] = 'enter'
    else:
        del dic[name]

result = sorted(dic.keys(), reverse=True)

for j in result:
    print(j)