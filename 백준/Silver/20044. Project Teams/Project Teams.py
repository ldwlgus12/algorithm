n = int(input())
w = list(map(int, input().split()))
lst = []
 
s_w = sorted(w)
r_w = sorted(w, reverse = True)
 
for i in range(len(w)):
    a = s_w[i] + r_w[i]
    lst.append(a)
    
print(min(lst))
