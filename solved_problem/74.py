t = int(input())
for i in range(t):
    n = int(input())
    s = input().split()
    for j in range(n):
        s[j] = int(s[j])
    s.sort(reverse=True)
    for j in range(n):
        flag = False
        for k in range(j+1,n - 1):
            if s[j] - s[k] in s[k+1:]:
                print(s[j])
                flag = True
                break
        if flag:
            break
    else:
        print(-1)