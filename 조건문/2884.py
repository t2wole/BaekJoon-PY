h ,m = map(int, input().split())

if h > 0 and m < 45:
    print(h - 1, m + 15)
elif m >= 45:
    print(h, m - 45)
else:
    print(23, m + 15)






    