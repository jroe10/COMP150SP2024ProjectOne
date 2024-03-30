import random
from character import Character
from location import Location

def game():
    answer = input('Would you like to play the game? (y/n) ')

    if answer.lower() == 'y':
        print('Welcome to the game!')
        inventory = []
        state = 'start'
        player_character = None 
        current_location = None

        while state != 'end':
            if state == 'start':
                print('Hello there! Welcome to the world of Comp150!')
                print('You are a student in this class, and you have to go on a quest to destroy the evil dragon!')

                choice = input('Do you accept this challenge? (y/n) ')
                if choice.lower() == 'y':
                    print('Great to hear it!')
                    print('You are going to need some armor in case you have to battle anyone')
                    inventory.append('Iron Armor')
                    print('You have your armor on and are ready to begin your quest')
                    
                    player_character = Character() 
                    print(f"You have been assigned the character {player_character.name}!")
                    
                    # Set the initial location for the player
                    current_location = Location(name="Starting Point", description="You are at the starting point of your journey.")
                    print(f"You are currently at: {current_location.name.get()} - {current_location.description.get()}")
                    
                    state = 'journey'
                else:
                    print('I understand that a quest is intimidating')
                    print('How about you get a computer and work from behind the scenes?')
                    inventory.append('Computer')
                    print('You can help your partner who is on the field from the safety of Mundy room 414')
                    state = 'rescue'

            elif state == 'journey':
                print('You are on your way to find the dragon...')
                print('Suddenly, you encounter a fork in the road.')
                fork_choice = input('Which path will you take? (left/right) ').lower()
                if fork_choice == 'left':
                    print('You chose the left path.')
                    print('As you venture deeper, you stumble upon a treasure chest.')
                    loot_choice = input('Do you open the chest? (y/n) ').lower()
                    if loot_choice == 'y':
                        print('You open the chest and find a shiny sword!')
                        inventory.append('Shiny Sword')
                        print('You take the sword and continue your journey.')
                    else:
                        print('You decide not to risk it and continue on your way.')
                elif fork_choice == 'right':
                    print('You chose the right path.')
                    print('You encounter a group of goblins blocking your way.')
                    action = input('Do you fight or try to sneak past? (fight/sneak) ').lower()
                    if action == 'fight':
                        print('You engage in a fierce battle with the goblins!')
                        print('After a tough fight, you emerge victorious.')
                        inventory.append('Goblin Ears')
                        print('You collect the goblin ears as trophies and continue your journey.')
                    elif action == 'sneak':
                        print('You attempt to sneak past the goblins...')
                        print('Unfortunately, one of the goblins spots you!')
                        decision = input('Will you fight? (y/n) ').lower()
                        if decision == 'y':
                            print('You engage in battle!')
                            # Continue the battle logic here
                        else:
                            print('You attempt to flee!')
                            # Implement the fleeing logic here
                    else:
                        print('Invalid choice!')
                else:
                    print('Invalid choice!')
                state = 'challenge'  # Transition to the challenge phase after completing the journey

            elif state == 'rescue':
                print('As you sit behind your computer, you receive a distress call from your partner.')
                print('They are surrounded by enemies and need your help!')
                rescue_choice = input('Will you go to their aid? (y/n) ').lower()
                if rescue_choice == 'y':
                    print('You decide to help your partner!')
                    print('You quickly gather your gear and rush to their location.')

                        # Implement additional rescue mission logic here

                    print('After a fierce battle, you successfully rescue your partner!')
                    print('Together, you both return safely to Mundy room 414.')
                    state = 'end'  # End the game after completing the rescue mission
                elif rescue_choice == 'n':
                    print('You choose not to go on the dangerous rescue mission.')
                    print('You continue to provide support from behind the scenes.')
                    state = 'end'  # End the game if not going on the rescue mission
                else:
                    print('Invalid choice! Please enter y or n.')

        print('Game over! Thanks for playing!')
    else:
        print('Okay, see you next time')

game()