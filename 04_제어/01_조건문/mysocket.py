import socket

ip = "192.168.10.60"
port = 21

s = socket.socket()
s.connect((ip, port))
ans = s.recv(1024)
print(ans)

if 'vsFTPd 2.3.4' in str(ans):
    print('Backdoor Command Execution')
elif 'vsFTPd 3.0.3' in str(ans):
    print('REMOTE Denail of servi e')
elif 'vsFTPd 2.0.5' in str(ans):
    print('deny_file Option Remote ouy of service')
else:
    print('Fail')