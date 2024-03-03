import random 

#def guess(x):
#    ans=random.randint(1,x)
#    guess=0
#    while guess!=ans:
#        guess=int(input(f'guess a number between 1 to {x}: '))
#        if guess<ans:
#            print('too low...')
#        else:
#            print('too high...')
#    print('congratulations!')

def computer_guess(x,cnt):
    while True:
        cnt+=1
        cguess=random.randint(1,100)
        print(f'I guess {cguess}')
        if cguess==x:
            print(f'I tried {cnt} times')
            break


#guess(10)
x=int(input('enter a number between 1 to 100: '))
computer_guess(x,0)