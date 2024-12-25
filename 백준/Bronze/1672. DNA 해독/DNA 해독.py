import sys
input = sys.stdin.readline

n = int(input())
string = list(input().rstrip())
dna = {"AG": "C", 
       "AC": "A", 
       "AT": "G", 
       "GC": "T", 
       "GT": "A", 
       "CT": "G", 
       "GA": "C", 
       "CA": "A", 
       "TA": "G", 
       "CG": "T", 
       "TG": "A", 
       "TC": "G"}

a = ""
b = string.pop()

for i in range(n-1):
    a = string.pop()
    if a == b:
        continue
        
    b = dna[a+b]
    
print(b)
