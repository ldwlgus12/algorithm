string = input()
n = int(input())
result = 0

for i in range(n):
    ring = input()
    
    if string in ring * 2:
        result += 1
        
print(result)