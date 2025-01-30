import sys
input = sys.stdin.readline

n = int(input())
word = input()
nums = ''
result = 0

for i in word:
    if '0' <= i and i <= '9':
        nums += i
    elif nums != '':
        result += int(nums)
        nums = ''
    
if nums != '':
    result += int(nums)

print(result)
        