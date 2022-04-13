n = int(input())

if n < 100: # 100보다 작은수는 모두 한수임
    print(n)
else:
    count = 0
    for i in range(100, n + 1):
        i = list(map(int, str(i)))
        if i[0] - i[1] == i[1] - i[2]:
            count += 1
    print(99 + count)

    