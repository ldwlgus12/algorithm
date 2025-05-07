n = int(input())
factorial = [1, 1]
Sum = 0

for i in range(2, 21):
    factorial.append(factorial[i-1] * i)

for i in range(20, -1, -1):
    if Sum+factorial[i] < n:
        Sum += factorial[i]
    elif Sum+factorial[i] == n:
        print("YES")
        exit(0)

print("NO")
