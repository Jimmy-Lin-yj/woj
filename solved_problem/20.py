a = list()
while True:
    try:
        a.append(input())
    except:
        break
total_cases = int(a[0])
cases_no = 0
for i in a[2::2]:
    cases_no += 1
    b = i.split()
    c = list()
    for j in range(len(b)):
        if j == 0:
            c.append(int(b[j]))
            continue
        c.append(int(b[j]) - int(b[j - 1]))
    c.sort()
    print("Case {0}:".format(cases_no))
    s = ""
    for num in c:
        if c.index(num) == 0:
            s += str(num)
            continue
        s += " {0}".format(num)
    print(s)
    if cases_no < total_cases:
        print("")