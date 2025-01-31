import sys
input = sys.stdin.readline

n, k = list(map(int, input().rsplit()))
lst = list(map(int, input().rsplit()))
cnt = 0
result = -1

for i in range(n-1, 0, -1):
	for j in range(i):
		if lst[j] > lst[j+1]:
			cnt += 1
			lst[j], lst[j+1] = lst[j+1], lst[j]

			if cnt == k:
				result = f'{lst[j]} {lst[j+1]}'	

print(result)
     