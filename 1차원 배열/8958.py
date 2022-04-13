n = int(input())

for i in range(n):
    ox_list = list(input())
    score = 0
    count = 0

    for ox in ox_list:
        if ox == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)


