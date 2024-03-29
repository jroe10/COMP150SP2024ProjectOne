def game():
    answer = input('Would you like to play the game? (y/n)')

    if answer.lower() == 'y':
        print('Welcome to the game!')
        start = True
        inventory = []

        print('Hello there! Welcome to the world of Comp150!')
        print('You are a student in this class, and you have to go on a quest to destroy the evil dragon!')

        choice = input('Do you accept this challenge? (y/n)')
        if choice.lower() == 'y':
            print('Great to hear it!')
            print('You are going to need some armor in case you have to battle anyone')
            inventory.append('Iron Armor')
            print('You have your armor on and are ready to begin your quest')

            while True:
                print('You are on your way to find the dragon...')
                print('Suddenly, you encounter a fork in the road.')
                fork_choice = input('Which path will you take? (left/right)')

                if fork_choice.lower() == 'left':
                    print('You chose the left path.')
                    print('As you venture deeper, you stumble upon a treasure chest.')
                    loot_choice = input('Do you open the chest? (y/n)')

                    if loot_choice.lower() == 'y':
                        print('You open the chest and find a shiny sword!')
                        inventory.append('Shiny Sword')
                        print('You take the sword and continue your journey.')
                    else:
                        print('You decide not to risk it and continue on your way.')
                elif fork_choice.lower() == 'right':
                    print('You chose the right path.')
                    print('You encounter a group of goblins blocking your way.')
                    action = input('Do you fight or try to sneak past? (fight/sneak)')

                    if action.lower() == 'fight':
                        print('You engage in a fierce battle with the goblins!')
                        print('After a tough fight, you emerge victorious.')
                        inventory.append('Goblin Ears')
                        print('You collect the goblin ears as trophies and continue your journey.')
                    elif action.lower() == 'sneak':
                        print('You attempt to sneak past the goblins...')
                        print('Unfortunately, one of the goblins spots you!')
                        print('You must fight or flee!')
                        decision = input('Fight or flee? (fight/flee)')
                        
                        if decision.lower() == 'fight':
                            print('You engage in battle!')
                            # Continue the battle logic here
                        elif decision.lower() == 'flee':
                            print('You attempt to flee!')
                            # Implement the fleeing logic here
                        else:
                            print('Invalid choice!')
                    else:
                        print('Invalid choice!')
                else:
                    print('Invalid choice!')
        else:
            print('I understand that a quest is intimidating')
            print('How about you get a computer and work from behind the scenes?')
            inventory.append('Computer')
            print('You can help your partner who is on the field from the safety of Mundy room 414')

        
            print('As you sit behind your computer, you receive a distress call from your partner.')
            print('They are surrounded by enemies and need your help!')

            rescue_choice = input('Will you go to their aid? (y/n)')

            if rescue_choice.lower() == 'y':
                print('You decide to help your partner!')
                print('You quickly gather your gear and rush to their location.')

                    # Implement additional rescue mission logic here

                print('After a fierce battle, you successfully rescue your partner!')
                print('Together, you both return safely to Mundy room 414.')
                return
            elif rescue_choice.lower() == 'n':
                print('You choose not to go on the dangerous rescue mission.')
                print('You continue to provide support from behind the scenes.')
                return
            else:
                print('Invalid choice! Please enter y or n.')
    else:
        print('Okay, see you next time')

game()