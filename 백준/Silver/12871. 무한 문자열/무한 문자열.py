s = input()
t = input()

len_s = len(s)
len_t = len(t)

if len_s * t == len_t * s:
    print(1)
else:
    print(0)