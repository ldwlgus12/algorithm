n = list(map(int,input().split()))
n_list = []
jegop = 0
result = 0

for i in range(len(n)):
    jegop = n[i] ** 2
    result += jegop
    
print(result%10)