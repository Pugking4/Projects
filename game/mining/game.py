from functions import *

def main():
    print("Welcome to the game")
    '''
    surface = gen.surface(7)
    for row in surface:
        print(' '.join(row))

    game_map = gen.mining_surface(7)
    for row in game_map:
        print(' '.join(row))
    '''
    surface_map = gen.surface(10)
    mining_surface_map = gen.mining_surface(10)

    combined_map = surface_map + mining_surface_map

    player_loc = player.init_player()

    for row in combined_map:
        if row == player_loc[1]:
            for cell in row:
                if cell == player_loc[0]:
                    cell = 'P'

    for row in combined_map:
        print(' '.join(row))



main()