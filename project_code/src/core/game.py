def game(): 
    answer= input('would you like to play the game? (y/n)')

    if answer.lower()=='y': 
        print('welcome to the game')
        start=True
        inventory=[]

        print('Hello there! Welcome to the world of Comp150!')
        print('You are a student in this class, and you have to go on a quest to destroy the evil dragon!')
        
        choice=input('Do you accept this challenge? (y/n)')
        if choice.lower() == 'y':
            choiceY1=True 
            print('Great to hear it!')
            print('You are going to need some armor in case you have to battle anyone')
            inventory.append('Iron Armor')
            print('You have your armor on and are ready to begin your quest')
            
            print('There is an individual on the path you are on. He may be dangerous. Do you wish to fight him or run?')
            decide=input('fight? (fight/run)')
            if decide.lower() == 'fight':
                print('You choose to fight!')
            elif decide.lower() == 'run':
                print('You choose to run!')
            else:
                print('Invalid choice!')
        else:
            choiceY1=False
            print('I understand that a quest is intimidating')
            print('How about you get a computer and work from behind the scenes?')
            inventory.append('Computer')
            print('You can help your partner who is on the field from the safety of Mundy room 414')
            
    else: 
        print('Okay, see you next time')

game()
                