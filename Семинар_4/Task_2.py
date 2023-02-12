bushes = int(input('Сколько кустов на грядке? -> '))
blueberry = []
max_blueberry = 0
for i in range(bushes):
    blueberry.append(i + 1)
print(blueberry)
for i in range(1, bushes - 1):
    if blueberry[i] + blueberry[i + 1] + blueberry[i - 1] > max_blueberry:
        max_blueberry = blueberry[i] + blueberry[i + 1] + blueberry[i - 1]
print(max_blueberry)