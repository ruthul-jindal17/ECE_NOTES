import os
a=int(input('player I : Enter the magic number:'))
os.system('cls')
c=0
while c<=10:
    b=int(input('Player II: Guess the magic number:'))
    if b==a:
        print('Great!!!')
        break
    elif b>a:
        print('higher')
        c=c+1
    elif a>b:
        print('lesser')
        c=c+1
if c==1:
    print('better luck nxt time!!')
