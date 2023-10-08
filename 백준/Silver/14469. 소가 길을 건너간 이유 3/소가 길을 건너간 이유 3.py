n = int(input())
lst = []
 
for i in range(n):
    a, b = map(int, input().split())
    lst.append([a, b])
 
lst.sort()
time = 0
 
for j in range(len(lst)):
    if time > lst[j][0]:	
        time = time + lst[j][1]	
    else:
        time = lst[j][0] + lst[j][1]
 
print(time)
