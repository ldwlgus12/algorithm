import sys 
input = sys.stdin.readline

n = int(input())
m_lose = list(map(int, input().split()))
m_lose.sort()
result = m_lose[-1]

if n%2 == 1:
    for i in range(n//2): 
        a = m_lose[i] + m_lose[n-i-2] 
        if result < a: 
            result = a
elif n%2 == 0:
    for i in range(n//2):
        a = m_lose[i] + m_lose[n-i-1]
        if result < a:
            result = a

print(result)
