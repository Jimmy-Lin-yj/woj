while True:
    s = input().split()
    if s == ['0'] * 3:
        break
    a = int(s[1]) * int(s[2])
    print(a if a > int(s[0]) else int(s[0]))