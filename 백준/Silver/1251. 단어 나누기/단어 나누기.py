word = list(input())
result = []

for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        first = word[:i]
        sec = word[i:j]
        thr = word[j:]

        first.reverse()
        sec.reverse()
        thr.reverse()

        result.append("".join(first+sec+thr))

print(min(result))