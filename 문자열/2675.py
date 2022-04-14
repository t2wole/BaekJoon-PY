t = int(input())

for i in range(t):
    count, word = input().split()
    for j in word:
        print(j * int(count), end='')
    print()

    