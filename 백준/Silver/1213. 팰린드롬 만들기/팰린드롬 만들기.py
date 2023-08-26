from collections import Counter

name = list(map(str,input()))
name.sort()
cnt = Counter(name)

mid = 0
mid_alpha = ''
result = ''

for i in cnt:
	if cnt[i] % 2 != 0:
		mid += 1
		mid_alpha += i

	for j in range(cnt[i]//2):
		result += i

if mid > 1:
	print("I'm Sorry Hansoo")
elif mid == 0:
	print(result + result[::-1])
else:
	print(result + mid_alpha + result[::-1])
    