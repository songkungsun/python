class Person:
	# 눈 두개, 코 하나, 입 하나 ....
	eyes = 2
	nose = 1
	mouth = 1
	ears = 2
	arms = 2
	legs = 2

	# 먹고 자고 이야기 하고....
	def eat(self):
		print('얌냠...')

	def sleep(self):
		print('쿨쿨...')

	def talk(self):
		print('주절주절...')


class Student(Person):
    def study(self):
        print('열공')

chan = Student()
print(chan.eyes)
print(chan.nose)

chan.sleep()
chan.study()




