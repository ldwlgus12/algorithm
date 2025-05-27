import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    x = int(''.join(list(input().split())))
    y = int(''.join(list(input().split())))
    data = list(map(int, input().split()))
    
    data += data[:m]
    result = 0

    for i in range(n):
        check = int(''.join(map(str, data[i:i+m])))
        if x <= check <= y:
            result += 1

    print(result)
    