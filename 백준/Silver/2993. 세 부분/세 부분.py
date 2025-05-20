words = input()
lst = []

for i in range(len(words)-2):
    for j in range(i+1, len(words)-1):
        for k in range(j+1, len(words)):
            a = words[:j][::-1] + words[j:k][::-1] + words[k:][::-1]
            lst.append(a)
            
print(min(lst))