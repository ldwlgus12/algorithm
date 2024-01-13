nums = set(range(1, 10000))
lst = set()

for i in nums :
    for j in str(i):
        i += int(j)
    lst.add(i) 

numbers = nums - lst 

for i in sorted(numbers):
    print(i)
    