while True:
    s = input().split()
    if s[0] == '0':
        break
    n = int(s[0])
    m = int(s[1])
    a = []
    for i in range(n):
        a.append(i+1)
    k = -1
    while len(a)>1:
        index = (m + k) % len(a)
        k = index - 1
        a.pop(index)
    print(a[0])