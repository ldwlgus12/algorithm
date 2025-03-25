import sys
input = sys.stdin.readline

m = [int(input()) for _ in range(10)]
score = 0
    
for i in m:
    score += i
    if score >= 100:
        if score - 100 > 100 - (score-i):
            score -= i
        break
        
print(score)
