n, k = map(int, input().split())
table = list(input())
cnt = 0

for i in range(n):
    if table[i] == 'P':
        for j in range(max(i-k, 0), min(i+k+1, n)):
            if table[j] == 'H':
                table[j] = 0
                cnt += 1
                break
                
print(cnt)
