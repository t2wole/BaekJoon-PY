C = int(input())

for i in range(C):
    N = list(map(int, input().split()))
    avg = sum(N[1:]) / N[0]
    count = 0

    for score in N[1:]:
        if score > avg:
            count += 1
    rate = (count / N[0]) * 100
    print('%.3f' %rate + '%')


