m, n = map(int, input().split())
lst = []
dict = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six',
        '7':'seven', '8':'eight', '9':'nine', '0':'zero'}

for i in range(m, n+1):
    a = ' '.join([dict[j] for j in str(i)])
    lst.append([i, a])
    
lst.sort(key=lambda x:x[1])

for k in range(len(lst)):
    if k % 10 == 0 and k != 0:
        print()
        
    print(lst[k][0], end=' ')