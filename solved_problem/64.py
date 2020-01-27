stdio = []
while True:
    try:
        stdio.append(input())
    except:
        break
for i in stdio[1::2]:
    s = i.split()
    for j in range(len(s)):
        s[j] = int(s[j])
    s = set(s)
    s = sorted(list(s))
    print(*s)