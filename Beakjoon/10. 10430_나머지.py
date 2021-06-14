A,B,C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)


#(A+B)%C는 ((A%C) + (B%C))%C 와 같은가?
#(A*B)%C는 ((A%C) * (B%C))%C 와 같은가?
# 결과: 1, 1, 0, 0
