import sys
input = sys.stdin.readline
p = int(input())

for _ in range(p):
    coin = {"TTT": 0, "TTH": 0, "THT": 0, "THH": 0, "HTT": 0, "HTH": 0, "HHT": 0, "HHH": 0}
    string = input()
    
    for i in range(38):
        coin[string[i:i+3]] += 1
    for a, b in coin.items():
        print(b, end=' ')
        
    print()
    