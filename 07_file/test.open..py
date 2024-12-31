from fileinput import filename

content = """Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!"""

fd = open('filename.txt', 'w')
fd.write(content)
fd.close()

fd = open('filename.txt')
lines = fd.readlines()
fd.close()

for line in lines:
    print(line, end='')
    