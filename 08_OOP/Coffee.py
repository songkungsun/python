class Coffee:
    total_amount  = 10
    total_amount_price = 5000
    coffee_price = 300
    put_price = 0
    req_coffee_nums = 0
    remaining_price = 0

    # def __init__(self, put_price, req_coffee_nums, remaining_price):
    #     self.requtest(put_price, req_coffee_nums, remaining_price)
    #     print('넣은 돈 : ', put_price)
    #     print('원하는 커피 개수 : ', req_coffee_nums)
    #     print('거스름 돈 : ', remaining_price)

    def request(self):
        put_price = int(input('돈을 넣어주세요 : '))
        req_coffee_nums = int(input('원하는 커피의 수를 입력해주세요 : '))
        self.put_price = put_price
        self.req_coffee_nums = req_coffee_nums


    def get(self):
        total_cost = self.req_coffee_nums * self.coffee_price
        if total_cost <= self.put_price:
            if Coffee.total_amount >= self.req_coffee_nums:
                self.remaining_price = self.put_price - total_cost
                if self.total_amount_price >= self.remaining_price:
                    Coffee.total_amount -= self.req_coffee_nums
                    self.total_amount_price -= self.remaining_price
                    print('커피를 %d 개 받아가세요' % self.req_coffee_nums)
                    print('거스름 돈 :', self.remaining_price)
                else:
                    print('거스름돈이 부족합니다. 관리자에게 연락해주세요. 죄송합니다.')
            else:
                print('재고가 부족합니다.')
        else:
            print('돈이 부족합니다.')

    def info(self):
        print('남은 커피 개수 :',self.total_amount)
        print('남은 돈 : ', self.total_amount_price)


shopping = Coffee()
while True:
    shopping.request()
    shopping.get()
    shopping.info()
    if Coffee.total_amount <= 0 or Coffee.total_amount_price <= 0:
        print('재고 또는 거스름돈이 다 떨어졌습니다. 확인해주세요 ')
        shopping.info()
        break