letters = list()
while True:
    try :
        letters.append(input())
    except:
        break   
for i in letters:
    comb = list()
    for j in range(len(i)):
        temp = i[j:] + i[:j]
        comb.append(temp)
    comb = sorted(comb)
    print(comb[0])
    