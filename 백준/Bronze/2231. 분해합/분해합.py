n = int(input())

for i in range(1, n+1):
    Sum = sum((map(int, str(i))))
    sum_num = i + Sum 
   
    if sum_num == n:
        print(i)
        break
        
    if i == n: 
        print(0)
        