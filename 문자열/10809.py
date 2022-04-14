s = input()
s_list = list(range(97, 123))   # a ~ z

for i in s_list:
    print(s.find(chr(i)))   #chr -> 숫자를 문자열로 변환

    