a = list()
num = list()
def init():
    num = list()
    for i in range(8):
        num.append(list())
    return num
while True:
    try:
        a.append(input())
    except:
        break
for i in range(len(a)):
    if i % 9 == 0 :
        num = init()
        continue
    animals = a[i].split()
    for j in animals:
        num[i%9 - 1].append(int(j))
    if i % 9 == 8 :
        value = 0
        for t in zip(*num):
            value += min(t)
        print(value)

    
