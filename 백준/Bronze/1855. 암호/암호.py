k = int(input())
string = input()
lst = []

for i in range(0, len(string), k*2):
    if i+k <= len(string):
        lst.append(string[i:i+k])

    if i + (k*2) <= len(string):
        lst.append(string[i + k:i + (k*2)][::-1])

result = ''

for i in range(k):
    for j in lst:
        result += j[i]

print(result)
