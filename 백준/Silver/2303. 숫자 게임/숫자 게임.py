n = int(input())
score = []

for _ in range(n):
    card = list(map(int, input().split()))
    max_nums = 0
    
    for i in range(5):
        for j in range(i+1, 5):
            for k in range(j+1, 5):
                nums = (card[i] + card[j] + card[k]) % 10
                if nums >= max_nums:
                    max_nums = nums
                    
    score.append(max_nums)

for i in range(n-1, -1, -1):
    if score[i] == max(score):
        print(i+1)
        break
        