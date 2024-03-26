k = bin(int(input()))[2:] 
result = 0

for i in range(len(k)):
    if int(k[i]) == 1:
        result += 3 ** (len(k)-i-1)
        
print(result)
