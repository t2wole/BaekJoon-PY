list = []

for i in range(10):
    numbers = int(input())
    list.append(numbers % 42)
    
list = set(list)
print(len(list))
