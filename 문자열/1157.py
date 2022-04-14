#결과를 대문자로 출력할거라 처음부터 upper해줌
words = input().upper()
words_list = list(set(words))   #['M','I','S','P']
cnt = []

for i in words_list:    # i = m, i, s, p
    count = words.count(i)
    cnt.append(count)   # cnt = [1, 4, 4, 1]

if cnt.count(max(cnt)) > 1: # 최대가 2개 이상이면
    print('?')
else:
    print(words_list[(cnt.index(max(cnt)))])

