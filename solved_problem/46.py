stdio = []
while True:
    try:
        stdio.append(input())
    except:
        break
case_no = int(stdio[0])
stdio.pop(0)
for i in range(case_no):
    count = 0
    stdio.pop(0)
    s = stdio[0].split()
    stdio.pop(0)
    for j in range(1,len(s) + 1):
        index = s.index(str(j))
        count += index + 1 - j
        temp = s[j - 1:index]
        s[j - 1:index + 1] = [str(j)] + temp
    print(count)