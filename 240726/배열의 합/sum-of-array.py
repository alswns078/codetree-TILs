arr = []

for i in range(4):
    arr.append(list(map(int, input().split())))

for item in arr:
    total = 0
    for i in item:
        total += i
    print(total)