N = int(input())
num = list(map(int, input().split()))
number = int(input())
result = 0


for i in range(len(num)):
    if number == num[i]:
        result += 1
  
print(result)