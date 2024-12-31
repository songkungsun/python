coffee=5
while True:
    input_money = int(input('money: '))
    sell_num = int(input('how many: '))
    if coffee ==0:
        break
    while True:
        if sell_num*500 >input_money:
            print('not enough money')
        elif sell_num*500 <= input_money:
            while True:
                if coffee-sell_num >= 0:
                    coffee=coffee-sell_num
                    print(sell_num,'get coffee')
                    break
                elif coffee-sell_num < 0:
                    print('not enough coffee')
                    print('retry')
            break