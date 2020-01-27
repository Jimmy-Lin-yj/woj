while True:
    n = int(input())
    if n == 0:
        break
    print("No Solution!" if n % 2 == 0 else "{}".format(n - 1))