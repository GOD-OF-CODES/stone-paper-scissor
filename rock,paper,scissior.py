import random,sys
wins=0
losses=0
ties=0
while True:
    print('your total wins='+str(wins))
    print('your total losses='+str(losses))
    print('your total ties='+str(ties))
    while True:
        print('enter your move rock(r), paper(p), scissor(s) or quit(q)')
        playermove=input()
        if playermove=='q':
            sys.exit()
        else :
            break
    if playermove=='r':
        print('rock versus.....')
    elif playermove=='p':
        print('paper versus.....')
    elif playermove=='s':
        print('scissor versus....')

    randomNumber=random.randint(1,3)
    if randomNumber==1:
        computermove='r'
        print('ROCK')
    elif randomNumber==2:
        computermove='p'
        print('PAPER')        
    elif randomNumber==3:
        computermove='s'
        print('SCISSOR')    

    if playermove == computermove :
        print('it is a tie')
        ties=ties+1
    elif playermove=='r' and computermove=='s':
        print('You won')
        wins=wins+1
    elif playermove=='r' and computermove=='p':
        print('you lose')
        losses=losses+1
    elif playermove=='p' and computermove=='r':
        print('you won')
        wins=wins+1
    elif playermove=='p' and computermove=='s':
        print('you lose')
        losses=losses+1
    elif playermove=='s' and computermove=='r':
        print('you lose')
        losses=losses+1
    elif playermove=='s' and computermove=='p':
        print('you win')
        wins=wins+1
