class Book:
    def __init__(self,title, price, author):
        print('new book')
        self.setData(title, price, author)

    def setData(self,title, price, author):
        self.tutle = title
        self.price = price
        self.author = author

    def printData(self):
        print(self.title)
        print(self.price)
        print(self.author)

b = Book()
b.setData('누가 내치즈먹음','300', '미키')
b.printData()