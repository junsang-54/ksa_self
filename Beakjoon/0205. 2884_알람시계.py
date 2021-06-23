# 틀림, 왜일까?

H, M = map(int, input().split())
if H > 0:
  if (M-45) < 0:
    print(H-1, M+15)
  elif (M-45) > 0:
    print(H, M-45)
elif H == 0:
  if (M-45) < 0:
    print(23, M+15)
  elif (M-45) > 0:
    print(H, M-45)
