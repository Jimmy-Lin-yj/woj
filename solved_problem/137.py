while True:
    try:
        money = int(input().split()[1])
        prices = input().split()
        prices.sort(key=lambda x:int(x))
        print(money//int(prices[0]))
    except:
        break