a = input().lower()
a_list = list(set(a))
cnt = []

for i in a_list:
    count = a.count(i)
    cnt.append(count)
if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(a_list[(cnt.index(max(cnt)))].upper())