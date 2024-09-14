n = list(map(int, input()))
half = len(n)//2
left = 0
right = 0

for i in range(0, half):
    left += n[i]
    
for i in range(half, len(n)):
    right += n[i]

if left == right:
    print("LUCKY")
else:
    print("READY")
    