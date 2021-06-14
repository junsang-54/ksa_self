a,b = input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)


#왜 오답일까
a, b = map(int, input().split())
print(int(a+b), '\n', int(a-b),'\n', int(a*b), '\n', int(a/b),'\n',int(a%b))
