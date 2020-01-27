nums = int(input())
for i in range(nums):
    xay = amr = 0
    a = input()
    line = []
    cards = input().split()
    for j in range(len(cards)):
        if  not cards[j] in line:
            line.append(cards[j])
        else:
            n = line.index(cards[j])
            m = len(line[n:]) + 1
            if j % 2 == 0:
                xay += m
            else:
                amr += m
            line = line[:n]
    print("xay") if xay > amr else print("amr")