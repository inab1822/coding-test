n = int(input())
plans = input().split()
X = 1
Y = 1


move_types = ['L','R','U','D']
R = 1
L = -1
U = -1
D = 1

# for i in plans:
#   if i == 'L' or i == 'R':
#     L = -1
#     R = 1
#     X += i
#     if X == 0 or X > n:
#       continue
#   else:
#     U = -1
#     D = 1
#     Y += i
#     if Y == 0 or Y > n:
#       continue
# print(X,Y) 
for i in plans:
  if i == 'L':
    if X == 1:
      continue
    else:
      X -= 1
  elif i == 'R':
    if X == n:
      continue
    else:
      X += 1
  elif i == 'U':
    if Y == 1:
      continue
    else:
      Y -= 1
  elif i =='D':
    if Y == n:
      continue
    else:
      Y += 1
print(X,Y)