nums = int(input())
month = (31,29,31,30,31,30,31,8)
for i in range(nums):
    s = input().split()
    m = int(s[0])
    d = int(s[1])
    days = 0
    for j in range(m,9):
        if j == m:
            days += month[j - 1] - d
        else:
            days += month[j - 1]
    print(days)