def chain_len(n:int):
    count = 1
    while n != 1:
        n = 3*n + 1 if n % 2 == 1 else n / 2
        count += 1
    return count
while True:
    s = input().split()
    i = int(s[0])
    j = int(s[1])
    if i == j == 0:
        break
    a = []
    for i in range(i,j+1):
        a.append(chain_len(i))
    print(max(a))