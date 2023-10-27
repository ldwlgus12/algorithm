n, m = map(int, input().split())
group = {}

for i in range(n):
    g_name = input()
    g_num = int(input())
    group[g_name] = [input() for _ in range(g_num)]

for j in range(m):
    name = input()
    if int(input()) == 1:
        for g_name, member in group.items():
            if name in member:
                print(g_name)
    else:
        print('\n'.join(sorted(group[name])))