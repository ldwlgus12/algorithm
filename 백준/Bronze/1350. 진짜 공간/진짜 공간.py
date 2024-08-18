n = int(input())
file = list(map(int, input().split()))
clu = int(input())
result = 0

for i in file :
  if i % clu > 0 :
    result += i//clu + 1
  else :
    result += i//clu

print(clu * result)
