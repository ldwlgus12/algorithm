for _ in range(int(input())):
	n, m = map(int, input().split())
	cnt = 0
    
	for i in range(n, m+1):
		for j in str(i):
			if j == '0':
				cnt += 1
                
	print(cnt)
    