import random

n, m = map( int, input().split())

result = list()
for i in range(n):
  i = list()
  for a in range(m):
    i.append(random.randrange(1,10000))
  print(i)
  result.append(min(i))

print(result)
print(max(result))