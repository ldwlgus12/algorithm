n, m = map(int, input().split())
n_name = set()
m_name = set()

for i in range(n):
    n_name.add(input())

for i in range(m):
    m_name.add(input())

result = sorted(list(n_name & m_name))

print(len(result))

for i in result:
    print(i)
    