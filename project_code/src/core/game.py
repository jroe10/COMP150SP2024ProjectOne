import random
from character import Character
from location import Location

starting_locations = ['Damen Student Center', 'Information Commons', 'Mundelien', 'Maddona della Strada', 'Metropolis Cafe']

def game():
    answer = input('Would you like to play the game? (y/n) ')

    if answer.lower() == 'y':
        print('Welcome to the game!')
        inventory = []
        state = 'start'
        player_character = None 
        starting_location = random.choice(starting_locations)  # Randomly choose a starting location

        while state != 'end':
            if state == 'start':
                print(f'You are currently at: {starting_location} - You are at the starting point of your journey.')
                print('Hello there! Welcome to the world of Comp150!')
                player_character = Character() 
                print(f"You have been assigned the character {player_character.name}!") 
                print('You are a student in this class, and you have to go on a quest to destroy the evil dragon.')
               

                choice = input('Do you accept this challenge? (y/n) ')
                if choice.lower() == 'y':
                    print('Great to hear it!')
                    print('You are going to need some armor in case you have to battle anyone.')
                    inventory.append('Iron Armor')
                    print('You have your armor on and are ready to begin your quest.')
                
                    state = 'journey'
                else:
                    print('I understand that a quest is intimidating.')
                    print('How about you get a computer and work from behind the scenes?')
                    inventory.append('Computer')
                    print('You can help your partner who is on the field from the safety of Mundy room 414.')
                    state = 'rescue'
                    
            elif state == 'journey':
                print('You set out on your journey, determined to find and defeat the evil dragon.')
                print('Along the way, you encounter various challenges and obstacles.')
                print('Your path is fraught with danger, but also opportunities for glory and treasure.')
                
                # Simulate a random encounter
                encounter_chance = random.randint(1, 10)
                if encounter_chance <= 5:  # 50% chance of encountering an enemy
                    print('Oh no! You encounter a fearsome enemy blocking your path!')
                    print('What will you do?')
                    action = input('Fight or flee? (fight/flee) ').lower()
                    if action == 'fight':
                        print('You engage in battle with the enemy!')
                        # Implement battle logic here
                        print('After a fierce battle, you emerge victorious!')
                        inventory.append('Enemy Loot')  # Add loot to inventory
                    elif action == 'flee':
                        print('You attempt to flee from the enemy!')
                        # Implement fleeing logic here
                        print('You manage to escape from the enemy and continue your journey.')
                    else:
                        print('Invalid choice! The enemy attacks while you hesitate!')
                        # Implement default action or penalty for invalid choice
                        print('You must fight!')
                        # Implement battle logic here
                        print('After a tough fight, you emerge victorious!')
                        inventory.append('Enemy Loot')  # Add loot to inventory
                else:
                    print('You continue your journey without any interruptions.')

                # You can add more encounters, choices, and challenges here
                print('You are on your way to find the dragon...')
                print('Choose your path:')
                print('1. Explore the forest')
                print('2. Investigate the castle ruins')
                print('3. Visit the nearby village')
                path_choice = input('Enter the number corresponding to your choice: ')
                if path_choice == '1':
                    print('You choose to explore the forest.')
                    # Implement forest exploration logic
                    # After completing forest exploration, transition to the next phase or location
                    state = 'next_phase_or_location'
                elif path_choice == '2':
                    print('You choose to investigate the castle ruins.')
                    print('You explore the ancient ruins, uncovering forgotten secrets and facing ancient guardians.')
                    print('You have successfully completed the first leg of your journey.')
                    print('You feel stronger and more determined than ever to face whatever lies ahead.')
                    # After completing castle ruins investigation, continue the game loop
                    state = 'next_phase_or_location'
                elif path_choice == '3':
                    print('You choose to visit the nearby village.')
                    # Implement village visit logic
                    # After completing village visit, transition to the next phase or location
                    state = 'next_phase_or_location'
                else:
                    print('Invalid choice! Please enter a number between 1 and 3.')


                print('You have successfully completed the first leg of your journey.')
                print('You feel stronger and more determined than ever to face whatever lies ahead.')
                state = 'next_phase_or_location'  # For now, we'll end the game after completing the journey

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