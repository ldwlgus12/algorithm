a,b,v = map(int, input().split())
day = (v-b)/(a-b)
print(int(day) if day == int(day) else int(day)+1)