import sys
N = int(sys.stdin.readline())
h_list = []
cnt = 0
hap = 0

for i in range(N):
    h_list.append(int(sys.stdin.readline()))
    
h_sort = h_list[::-1]
for j in range(len(h_sort)):
    if hap < h_sort[j]:
        cnt += 1
        hap = h_sort[j]

print(cnt)