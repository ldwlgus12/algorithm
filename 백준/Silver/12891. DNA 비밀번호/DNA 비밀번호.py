from collections import deque

s, p = map(int, input().split())
string = list(str(input()))
A, C, G, T = map(int, input().split())

dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
left, right = 0, p-1
queue = deque(string[left:right])
cnt = 0

for i in queue:
    dic[i] += 1

while right < s:
    dic[string[right]] += 1

    if dic['A'] >= A  and dic['C'] >= C and dic['G'] >= G and dic['T'] >= T:
        cnt += 1    
        
    dic[string[left]] -= 1
        
    left += 1
    right += 1

print(cnt)