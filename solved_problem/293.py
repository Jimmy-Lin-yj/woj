while True:
    a = input().split()
    m = int(a[0])
    n = int(a[1])
    if n == m == 0:
        break
    a = []
    for i in range(n):
        a.append([])
    for i in range(n):
        for j in range(i + 1):
            a[n - 1 - i + j].append(str(m) if m>9 else " " + str(m))
            m += 1
    for i in a:
        i.append("")
    for i in a:
        print(*i)
    print("")