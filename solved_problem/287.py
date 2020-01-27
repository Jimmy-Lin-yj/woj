a = [0] * 51
a[0] = a[2] = 1
for i in range(4,51,2):
    for j in range(0,i - 1,2):
        a[i] += a[j] * a[i - 2 - j]
while True:
    try:
        n = int(input())
        print(a[n])
    except:
        break   