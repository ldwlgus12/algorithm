name = input()
n = int(input())
lst = sorted([input() for i in range(n)])
a, b = 0, 0

for i in range(n):
    L = name.count("L") + lst[i].count("L")
    O = name.count("O") + lst[i].count("O")
    V = name.count("V") + lst[i].count("V")
    E = name.count("E") + lst[i].count("E")
    
    win = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    
    if a < win:
        a = win
        b = i
        
print(lst[b])
