file = open('names.txt', 'r')
list = {}
for i in range(5000):
    for n in file.readline().split():
        list[i] = n

print(list)