import random

char = ['samurai', 'cowboy', 'knight']
characters = [characters.title() for characters in char]
damage = [dmg for dmg in range(1,11)]
cur_health = [10] 

print('------------')
print('TEXT WARRIOR')
print('------------')

print(f'Greetings Vagabond, CHOOSE YOUR WARRIOR {characters}'.center(10))

def battle_phase():
    action = input('Would you like to attack? (y/n)')
    if action.lower() == 'n':
        print('Bye')
        exit()

    while action.lower() == 'y':
        try: 
            ran_dmg = random.choice(damage)
            cur_health[0] -= ran_dmg
            if cur_health[0] > 0:
                print(f'Enemy Health: {cur_health}')
                battle_phase()
            if cur_health[0] < 0:
                print('ENEMY FELL')
                break
        except:
             print('Invalid action')
             exit()
    else:
        print('[y] or [n] only')
        battle_phase()

def pick_screen():
    char_choice = input()
    if char_choice.title() == characters[0]:
        print(f'You are the {characters[0]}')
        battle_phase()
        quit()
    if char_choice.title() == characters[1]:
        print(f'You are the {characters[1]}')
        battle_phase()
        quit()
    if char_choice.title() == characters[2]:
        print(f'You are the {characters[2]}')
        battle_phase()
        quit()
    else:
        print('Invalid input')
        del char_choice
        pick_screen()

pick_screen()