card = [i for i in range(21)]

for i in range(10):
    a, b = map(int, input().split())
    
    for j in range((b - a + 1) // 2):
        n = card[b-j]
        card[b-j] = card[a+j]
        card[a+j] = n
        
for i in card[1:]:
    print(i, end=' ')
    