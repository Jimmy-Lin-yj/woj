stdio = []
def convert(n):
    s = bin(int(n))
    if s.count("1") % 2 == 0:
        return 0
    else:
        return 1
while True:
    try:
         n = int(input())
         for i in range(n):
             s = input().split()
             temp = []
             for j in s:
                 temp.append(convert(j))
             stdio.append(temp)
    except:
        break
for i in stdio:
    print(*i)