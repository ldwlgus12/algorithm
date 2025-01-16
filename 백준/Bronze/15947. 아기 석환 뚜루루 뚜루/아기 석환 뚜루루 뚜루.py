lst = ["baby", "sukhwan", "tururu", "turu", "very", "cute", "tururu", 
      "turu", "in", "bed", "tururu", "turu", "baby", "sukhwan"]
n = int(input())-1
a = n//14

if n%14 in [3, 7, 11]:
    print(f"tu+ru*{a+1}" if a >= 4 else "turu"+"ru"*a)    
elif n%14 in [2, 6, 10]:
    print(f"tu+ru*{a+2}" if a >= 3 else "tururu"+"ru"*a)    
else:
    print(lst[n%14])
        