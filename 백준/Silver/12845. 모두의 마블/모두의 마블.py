import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
a = l[0]
gold = 0

for i in range(1, len(l)) :
    gold += (a + l[i])

print(gold)
