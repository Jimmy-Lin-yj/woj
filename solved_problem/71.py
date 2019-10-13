while True:
    try:
        s = input().split()
        n = int(s[0])
        m = int(s[1])
        a = []
        b = []
        for i in range(n):
            a.append(i+1)
        key = 0
        while len(a) > 1:
            i = (key + m)%len(a)
            b.append(a[i - 1])
            a.pop(i - 1)
            key = i - 1 if i > 1 else 0 
        b.append(a[0])
        print(*b)
    except:
        break