import string
a = string.ascii_lowercase
t = int(input())
for i in range(t):
    s = input().split()
    d = []
    for j in range(len(s[0])):
        d.append(abs(a.index(s[0][j]) - a.index(s[1][j])))
    d.sort(reverse=True)
    for j in range(int(s[2])):
        if d[j] == 0:
            d[j] = 1
        else:
            d[j] = 0
    print(sum(d))