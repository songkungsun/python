
def add():
    print('add')

def delete():
    print('del')

def list():
    print(list)

prompt="""
1. add
2. del
3. list
4. quit
"""
while True:
    print(prompt)
    choice = input('enter your number: ' )
    if choice == '1':
        add()
    elif choice =='2':
        delete()
    elif choice == '3':
        list()
    elif choice == '4':
        break
    else:
        print('FAIL, Retry')

