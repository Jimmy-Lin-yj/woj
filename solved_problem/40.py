stdio = []
while True:
    try:
        stdio.append(input())
    except:
        break
cases_no = int(stdio[0])
stdio.pop(0)
for i in range(cases_no):
    stdio.pop(0)
    s = stdio[0]
    stdio.pop(0)
    mgbuild = s.split()
    mglist = []
    while len(mgbuild) != 0:
        temp = set()
        for j in mgbuild:
            temp.add(j)
        for j in temp:
            mgbuild.remove(j)             
        mglist.append(temp)
    print(len(mglist))