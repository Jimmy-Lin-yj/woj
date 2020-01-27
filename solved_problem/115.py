import string
stdio = []
while True:
    a = input()
    if a == "R0C0":
        break
    row = a.split('C')[0][1:]
    colum = int(a.split('C')[1])
    temp = ""
    while colum > 0:
        n = colum % 26
        if n == 0:
            n = 26
            colum -= 1
        colum //= 26
        temp += string.ascii_uppercase[n - 1]
    print(temp[::-1] + row)