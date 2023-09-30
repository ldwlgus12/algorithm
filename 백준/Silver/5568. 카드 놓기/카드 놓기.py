from itertools import permutations

n, k = int(input()), int(input())
card = []

for i in range(n):
    num = input()
    card.append(num)

result = set()

for j in permutations(card, k):
    result.add(''.join(j))

print(len(result))
