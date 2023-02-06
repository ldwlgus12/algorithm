people = [list(map(int, input().split())) for _ in range(4)]
hap = 0
result = []

for i in range(len(people)):
    hap =  hap - people[i][0]
    hap =  hap + people[i][1]
    result.append(hap)

print(max(result))