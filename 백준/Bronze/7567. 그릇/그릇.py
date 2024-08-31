plate = list(str(input()))
result = 0

for i in range(len(plate)):
    if i == 0:
        result += 10
    elif plate[i] == plate[i-1]:
        result += 5
    else:
        result += 10
        
print(result)
