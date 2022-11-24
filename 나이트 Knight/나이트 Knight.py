x = ['a','b','c','d','e','f','g','h']
y = [1,2,3,4,5,6,7,8]
cx = x.index(input()) + 1
cy = int(input())
move_way = [
(cx+2, cy+1),
(cx+2, cy-1),
(cx-2, cy-1),
(cx-2, cy+1),
(cx-1, cy+2),
(cx+1, cy+2),
(cx+1, cy-2),
(cx-1, cy-2)
]
count = 0
for i in move_way:
  if any([i[0] <= 0, i[1] <= 0, i[0] > 8, i[1] > 8]):
    continue
  else:
    count += 1
print(count)