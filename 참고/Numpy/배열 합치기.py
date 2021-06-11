c = np.concatenate((a,b), axis=1)

# a, b는 배열, axis는 추가하고싶은 축 선택
# c = [(a배열), (b배열)]


#여러 행렬 합칠 때
# 1안. concatenate n번 호출
for i in range(n):
  a = np.concatenate((a,b), axis=1)
  
# 2안. list를 이용해 append하고, 마지막에 형상변형
a = []
for i in range(n):
  b = np.array()
  a.append(b)
  
a = np.array(a)

# 1안 보다 2안이 시간 단축됨
