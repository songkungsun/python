class Fridge:
    isOpened = False
    foods =[]

    def open(self):
        self.isOpened = True
        print('문열림')

    def put(self, things):
        if self.isOpened:
            self.foods.append(things)
            print('냉장고에 %s 을 넣었습니다.' % things)
        else:
            print('Fail 냉장고 문이 닫혀 있습니다 ')

    def close(self):
        self.isOpened = False
        print('문닫힘')
class Food:
    pass