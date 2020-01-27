t = int(input())
for i in range(t):
    s = input()
    x = y = sum = 0
    for j in s:
        if j == 'U':
            y += 1
        else:
            sum += y
            x += 1
    area = x * y / 2
    area -= sum
    print("{0:0<.3f}".format(area))