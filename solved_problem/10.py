stdio = []
while True:
    s = input()
    if s == '0':
        break
    stdio.append(s)
for i in stdio[1::2]:
    i = i.split()
    for j in range(len(i)):
        i[j] = int(i[j])
    m = max(i)
    print(m * 2 ** (len(i) - 1) % 2006)