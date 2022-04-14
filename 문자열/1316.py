
n = int(input())
groupWord = 0

for i in range(n):
    word = input()
    for j in range(len(word)):
        if j != len(word) - 1:
            if word[j] == word[j + 1]:
                pass
            elif word[j] in word[j + 1:]:
                break
        else:
            groupWord += 1
print(groupWord) 


