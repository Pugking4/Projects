import random
from colored import fg, style
import textwrap
import time
from functions import *



death = 0
map_size = 5

def start_game():
    print("Welcome to the game!")
    print("To see commands type 'help'")
    game_map = gen.create_game_map(map_size)
    room_counts = gen.random_room_count()
    coords = gen.generate_coords(map_size)
    gen.assign_random_coords(game_map, room_counts, coords)
    room_desc, monster_rooms = gen.assign_description_to_rooms(game_map)
    money, bank, bank_int = game_init.initialize_money()
    player = game_init.initialize_stats()
    monster_out = comgen.generate_random_monster_stats(monster_rooms)
    #find entrance and assign to player loc
    for row in game_map:
        for room in row:
            if room == 5:
                #player loc is the coords of the entrance
                player_loc = [game_map.index(row), row.index(room)]
    return game_map, player_loc, money, bank, bank_int, player, room_desc, monster_rooms, monster_out

game_map, player_loc, money, bank, bank_int, player, room_desc, monster_rooms, monster_out = start_game()

old_display_loc = f'[{player_loc[1]}, {player_loc[0]}]'

while True:
    display_loc = f'[{player_loc[1]}, {player_loc[0]}]'
    action = input("What would you like to do? ")
    act.action_event(player_loc, game_map, room_desc, action, bank_int, old_display_loc, monster_out, player)
    if death == 1:
        break
    old_player_loc = player_loc
    old_display_loc = f'[{old_player_loc[1]}, {old_player_loc[0]}]'
    bank = act.interest(bank, bank_int)

#print_map(game_map, player_loc)
#print("Thanks for playing!")
print("bruh")


#balance player stats (too weak) or nerf monsters (too strong)
#add actions to rooms (interact, open, close, etc.)
#add shop items
#implement items into combat system
#add ending text
#add fishing (high priority)
#implement monster abilities into combat system

#add 3rd dimension??
