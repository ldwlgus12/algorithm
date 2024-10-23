s = list(input())
pw = list(input())

for i in range(len(s)):
    if 97 <= ord(s[i]) <= 122:
        s[i] = chr(((ord(s[i]) - ord(pw[i % len(pw)]) - 1) % 26) + 97) 
        
print("".join(s))