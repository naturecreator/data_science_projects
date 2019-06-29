# Rock paper scissors game

print('''Pick one from the following:
            rock
            scissors
            paper''')

while True:
    dict_game = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("Player a: "))
    player_b = str(input("Player b: "))
    a = dict_game.get(player_a)
    b = dict_game.get(player_b)
    difference = a - b

    if difference in [-1, 2]:
        print('player a wins')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over')
            break
    elif difference in [-2, 1]:
        print('player b wins')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over')
            break
    else:
        print('It is a draw. Please continue the game')
        print('')
