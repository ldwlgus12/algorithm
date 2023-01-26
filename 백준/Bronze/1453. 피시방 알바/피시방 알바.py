N = int(input())
num = list(map(int, input().split()))
number = len(set(num))

print(N-number)