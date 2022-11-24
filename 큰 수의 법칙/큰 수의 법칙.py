# 공백으로 구분하여 입력받기
n, m, k = map( int , input().split() )
data = list( map( int , input().split() ) )

result = 0

data.sort(reverse=True)
first, second = data[0], data[1]

while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1
  if m == 0:
    break
  result += second
  m -= 1

print(result)