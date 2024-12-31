filenames = ['intra.h', 'intra.c', 'input.txt', 'run.py']
result= []
for name in filenames:
    extention = name.split('.')[-1]
    if extention == 'h' or extention == 'c':
        print(extention)
        result.append(name)
print(result)