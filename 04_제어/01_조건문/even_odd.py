num1 = int(input('입력1: '))
num2 = int(input('입력2: '))

if num1 > num2:
    big = num1
elif num1 < num2:
    big = num2
else:
    big = 'equal'

print('big num :', big)

if (big % 2) == 0:
    even = '짝수'
else:
    even = '홀수'
print(even)


