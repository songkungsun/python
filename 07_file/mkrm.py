import os


contents = """반갑습니다. 파이썬 개발자 여러분
한살 더 드셨죠!
올 한해는 행복한 가득한 한해가 되었으면 합니다.
"""
os.system('mkdir -p ./test')
file = './test/test.txt'

fd = open(file,'w')
fd.write(contents)
fd.close()

fd = open(file,'r')
lines = fd.readlines()
for line in lines:
    print(line, end='')
fd.close()

if os.path.exists(file):
    os.remove(file)
    print('well delete')
