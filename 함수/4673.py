def d(n):
    n = n + sum(map(int, str(n)))
    return n

# 셀프넘버 아닌 수들의 집합
nonSelfNum = set()

# nonSelfNum 에 들어갈 수들 찾기
for i in range(1, 10001):
    nonSelfNum.add(d(i))

# 셀프 넘버 출력하기
for j in range(1, 10001):
    if j not in nonSelfNum:
        print(j)


