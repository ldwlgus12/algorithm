def check(now, seq):
  if abs(ord(now[0]) - ord(seq[0])) == 2 and abs(int(now[1]) - int(seq[1])) == 1:
    return 1
  elif abs(ord(now[0]) - ord(seq[0])) == 1 and abs(int(now[1]) - int(seq[1])) == 2:
    return 1
  else:
    return 0

route = []
now = input()
route.append(now)
cnt = 1

for i in range(35):
    seq = input()
    route.append(seq)

    if check(now, seq) == 1:
        cnt += 1
        now = seq
    else:
        break

if cnt == 36 and len(set(route))== 36 and check(route[0], route[-1]):
    print('Valid')
else:
    print('Invalid')
