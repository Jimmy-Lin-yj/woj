stdio = []
while True:
    s = int(input())
    if s == 0:
        break
    stdio.append(s)
for n in stdio:
    if n <= 3:
        print(n)
    elif n == 4:
        print("2 2")
    else:
        div , mod = divmod(n,3)
        s = ''
        if mod == 1:
            div -= 1
            s += '2 2 '
        if mod == 2:
            s += '2 '
        for i in range(div):
            if i == 0:
                s += '3'
            else:
                s += ' 3'
        print(s)