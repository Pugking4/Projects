import random
from colored import fg, style
import textwrap
import time

map_size = 5
admin = 1
generate_random_monster_count = -1
death = 0

#assign colors to room types
blue = fg('blue')
red = fg('red')
green = fg('green')
yellow = fg('yellow')
magenta = fg('magenta')
cyan = fg('cyan')
black = fg('black')
reset = style.RESET


def create_game_map(map_size):
    game_map = [[0 for x in range(map_size)] for y in range(map_size)]
    return game_map

room_types = {
    0: {0: "Empty"},
    1: {1: "Treasure"},
    2: {2: "Monster"},
    3: {3: "Boss"},
    4: {4: "Shop"},
    5: {5: "Entrance"},
    6: {6: "Exit"}
}
def random_room_count():
    room_counts = {}
    for room_type in room_types:
        if room_type == 1 or room_type == 2:
            rand = random.randint(3, 6)
            room_counts[room_type] = rand
        elif room_type == 3:
            rand = random.randint(0, 2)
            room_counts[room_type] = rand
        elif room_type == 4:
            rand = random.randint(1, 2)
            room_counts[room_type] = rand
        elif room_type == 5 or room_type == 6:
            room_counts[room_type] = 1
    return room_counts

axis = ['0', '1', '2', '3', '4']

def generate_coords(map_size):
    coords = []
    for i in range(map_size):
        for j in range(map_size):
            coords.append([i, j])
    return coords

def assign_random_coords(game_map, room_counts, coords):
    dupe_check = []
    for room_type in room_counts:
        flag = True
        for i in range(room_counts[room_type]):
            flag = True
            while flag:
                rand = random.choice(coords)
                if rand not in dupe_check:
                    dupe_check.append(rand)
                    flag = False
                    game_map[rand[0]][rand[1]] = room_type

def help():
    print("Commands: help, {move: forward, backward, left, right}, quit, map")

def print_map(game_map, player_loc):
    print('   ' + ' '.join(axis))
    print('   ' + '_' * (len(' '.join(axis))))
    for count, row in enumerate(game_map):
        new_row = []
        for i, cell in enumerate(row):
            if [count, i] == player_loc:
                new_row.append(blue + str(cell) + reset)
            elif cell == 1:
                new_row.append(yellow + str(cell) + reset)
            elif cell == 2:
                new_row.append(red + str(cell) + reset)
            elif cell == 3:
                new_row.append(magenta + str(cell) + reset)
            elif cell == 4:
                new_row.append(cyan + str(cell) + reset)
            elif cell == 0:
                new_row.append(black + str(cell) + reset)
            else:
                new_row.append(str(cell))
        print(str(count)+'|', ' '.join(new_row))
    print(f"Player location: [{player_loc[1]}, {player_loc[0]}]\nRoom type: {room_types[game_map[player_loc[0]][player_loc[1]]][game_map[player_loc[0]][player_loc[1]]]}")

def move_player(action, player_loc, game_map, old_display_loc):
    if action == "forward" or action == "f":
        if player_loc[0] == 0:
            print("You can't move forward")
        else:
            player_loc[0] -= 1
            display_loc = f'[{player_loc[1]}, {player_loc[0]}]'
            print(f'You moved from {old_display_loc} to {display_loc}')
            print_map(game_map, player_loc)
    elif action == "backward" or action == "b":
        if player_loc[0] == map_size-1:
            print("You can't move backward")
        else:
            player_loc[0] += 1
            display_loc = f'[{player_loc[1]}, {player_loc[0]}]'
            print(f'You moved from {old_display_loc} to {display_loc}')
            print_map(game_map, player_loc)
    elif action == "left" or action == "l":
        if player_loc[1] == 0:
            print("You can't move left")
        else:
            player_loc[1] -= 1
            display_loc = f'[{player_loc[1]}, {player_loc[0]}]'
            print(f'You moved from {old_display_loc} to {display_loc}')
            print_map(game_map, player_loc)
    elif action == "right" or action == "r":
        if player_loc[1] == map_size-1:
            print("You can't move right")
        else:
            player_loc[1] += 1
            display_loc = f'[{player_loc[1]}, {player_loc[0]}]'
            print(f'You moved from {old_display_loc} to {display_loc}')
            print_map(game_map, player_loc)
    else:
        print("Invalid command")
    return player_loc

import random

def generate_empty_room_description():
    adjectives = [
        "dimly lit",
        "dark",
        "spacious",
        "cramped",
        "musty",
        "echoing",
        "damp",
    ]

    features = [
        "cobwebs in the corners",
        "cracked walls",
        "peeling paint",
        "a single flickering torch",
        "dusty floorboards",
        "a mysterious draft",
        "piles of debris",
    ]

    phrases = [
        "It looks like no one has been here in ages.",
        "The silence is eerie.",
        "You feel a chill down your spine.",
        "The air is heavy with anticipation.",
        "You can almost hear whispers in the wind.",
        "You feel a sense of emptiness.",
        "It's hard to shake the feeling that you're being watched.",
    ]

    adj = random.choice(adjectives)
    feature = random.choice(features)
    phrase = random.choice(phrases)

    description = f"This {adj} room has {feature}. {phrase}"

    return description

def generate_treasure_room_description():
    adjectives = [
        "sparkling",
        "ancient",
        "glistening",
        "mysterious",
        "shiny",
        "ornate",
        "dazzling",
    ]

    items = [
        "gold coins",
        "jewels",
        "gemstones",
        "silver bars",
        "artifacts",
        "relics",
        "rare books",
    ]

    phrases = [
        "covered in a layer of dust",
        "strewn about haphazardly",
        "neatly organized on shelves",
        "piled up in the corner",
        "hidden in secret compartments",
        "guarded by a magical aura",
        "arranged in intricate patterns",
    ]
    
    ending_phrases = [
        "It's a sight to behold!",
        "You can hardly believe your eyes!",
        "You've never seen anything like it!",
        "It's a treasure hunter's dream!",
        "The wealth in this room is staggering!",
        "You feel a rush of excitement!",
        "You're left in awe at the sight!",
    ]
    
    adj1 = random.choice(adjectives)
    adj2 = random.choice(adjectives)
    item1 = random.choice(items)
    item2 = random.choice(items)
    phrase = random.choice(phrases)
    ending = random.choice(ending_phrases)

    # Ensure that the two adjectives and items are different
    while adj1 == adj2:
        adj2 = random.choice(adjectives)
    while item1 == item2:
        item2 = random.choice(items)

    description = (
        f"This room is filled with {adj1} {item1} and {adj2} {item2}, "
        f"all {phrase}. {ending}"
    )

    return description

def generate_monster_room_description(monster):
    adjectives = [
        "dimly lit",
        "dark",
        "spacious",
        "cramped",
        "musty",
        "echoing",
        "damp",
    ]

    actions = [
        "prowling around",
        "lurking in the shadows",
        "growling menacingly",
        "snarling aggressively",
        "scratching at the walls",
        "gnashing its teeth",
        "staring you down",
    ]

    phrases = [
        "You feel a sense of dread.",
        "The air is thick with tension.",
        "You can sense its hunger.",
        "Your heart races in fear.",
        "You can't help but shiver.",
        "You brace yourself for a fight.",
        "The atmosphere is charged with danger.",
    ]

    adj = random.choice(adjectives)
    action = random.choice(actions)
    phrase = random.choice(phrases)

    description = f"This {adj} room is occupied by a {monster}, {action}. {phrase}"

    return description, monster+str(generate_random_monster_count)

def generate_random_monster(generate_random_monster_count):
    monsters = [
        "vicious werewolf",
        "bloodthirsty vampire",
        "ferocious dragon",
        "sinister ghost",
        "giant spider",
        "slime creature",
        "skeleton warrior",
    ]

    return random.choice(monsters), generate_random_monster_count + 1

def generate_random_boss():
    bosses = [
        "fearsome dragon king",
        "malevolent lich",
        "enormous kraken",
        "ancient sphinx",
        "powerful demon lord",
        "mighty cyclops",
        "cunning vampire lord",
    ]

    return random.choice(bosses)

def generate_boss_room_description(boss):
    adjectives = [
        "massive",
        "dark",
        "opulent",
        "ominous",
        "eerie",
        "imposing",
        "threatening",
    ]

    phrases = [
        "covered in shadows",
        "filled with the echoes of the defeated",
        "illuminated by flickering torchlight",
        "dominated by a huge throne",
        "littered with bones and debris",
        "adorned with trophies of past conquests",
        "surrounded by an air of dread",
    ]

    ending_phrases = [
        "The tension in the air is palpable.",
        "You feel a chill down your spine.",
        "Your heart races as you prepare for battle.",
        "This is the moment you've been waiting for.",
        "You take a deep breath and ready your weapon.",
        "There's no turning back now.",
        "You know the fight ahead will be difficult.",
    ]

    adj = random.choice(adjectives)
    phrase = random.choice(phrases)
    ending = random.choice(ending_phrases)

    description = (
        f"This {adj} room is the lair of the {boss}, "
        f"{phrase}. {ending}"
    )

    return description

def generate_random_shopkeeper():
    shopkeepers = [
        "wizened old wizard",
        "mysterious cloaked figure",
        "grumpy dwarf merchant",
        "cheerful elven trader",
        "talkative goblin vendor",
        "quiet half-orc shopkeeper",
        "well-dressed human aristocrat",
    ]

    return random.choice(shopkeepers)

def generate_random_item():
    items = [
        "healing potions",
        "magical scrolls",
        "enchanted weapons",
        "mysterious artifacts",
        "protective amulets",
        "rare spellbooks",
        "various trinkets",
    ]

    return random.choice(items)

def generate_shop_room_description(shopkeeper, item):
    adjectives = [
        "cramped",
        "cozy",
        "welcoming",
        "cluttered",
        "dimly lit",
        "intriguing",
        "well-organized",
    ]

    phrases = [
        "lined with shelves",
        "filled with the scent of incense",
        "illuminated by warm candlelight",
        "packed with intriguing items",
        "displaying a wide array of wares",
        "decorated with colorful tapestries",
        "filled with the sounds of wind chimes",
    ]

    ending_phrases = [
        "You feel a sense of curiosity.",
        "It's easy to lose track of time in here.",
        "You can't help but browse the wares.",
        "You might just find something useful.",
        "You wonder what treasures await.",
        "You hope to find a valuable item.",
        "There's so much to explore.",
    ]

    adj = random.choice(adjectives)
    phrase = random.choice(phrases)
    ending = random.choice(ending_phrases)

    description = (
        f"This {adj} shop is run by a {shopkeeper}, "
        f"with {item} on display. The room is {phrase}. {ending}"
    )

    return description

def generate_entrance_room_description():
    surroundings = [
        "a dense forest",
        "a barren wasteland",
        "a desolate mountain range",
        "a misty swamp",
        "a peaceful meadow",
        "a sandy desert",
        "a rocky coastline",
    ]

    atmospheres = [
        "an eerie silence",
        "the sound of distant howls",
        "the rustling of leaves",
        "a soft breeze",
        "an unsettling fog",
        "a sense of foreboding",
        "a feeling of tranquility",
    ]

    adjectives = [
        "ancient",
        "mysterious",
        "welcoming",
        "abandoned",
        "ominous",
        "weathered",
        "intriguing",
    ]

    phrases = [
        "made of weathered stone",
        "carved from solid rock",
        "guarded by crumbling statues",
        "marked with arcane symbols",
        "hidden beneath overgrown vines",
        "covered in moss and lichen",
        "illuminated by flickering torches",
    ]

    ending_phrases = [
        "You wonder what lies ahead.",
        "You take a deep breath and prepare for adventure.",
        "You feel a mixture of excitement and trepidation.",
        "You step forward, eager to explore.",
        "You brace yourself for the challenges ahead.",
        "You can't help but feel a sense of anticipation.",
        "Your heart races as you enter.",
    ]

    surrounding = random.choice(surroundings)
    atmosphere = random.choice(atmospheres)
    adj = random.choice(adjectives)
    phrase = random.choice(phrases)
    ending = random.choice(ending_phrases)

    description = (
        f"You stand at the entrance of a {adj} structure, "
        f"surrounded by {surrounding}. The air is filled with {atmosphere}. "
        f"The entrance is {phrase}. {ending}"
    )

    return description

def generate_exit_room_description():
    surroundings = [
        "a serene garden",
        "a hidden cave",
        "an open clearing",
        "a mystical portal",
        "a narrow passageway",
        "a secret door",
        "a grand staircase",
    ]

    atmospheres = [
        "a sense of accomplishment",
        "a feeling of relief",
        "a calm and peaceful air",
        "the sound of celebration",
        "a gentle wind",
        "a quiet hush",
        "a feeling of triumph",
    ]

    adjectives = [
        "ancient",
        "mysterious",
        "welcoming",
        "hidden",
        "ominous",
        "illuminated",
        "inviting",
    ]

    phrases = [
        "marked with ancient runes",
        "shrouded in a soft glow",
        "decorated with intricate carvings",
        "guarded by a magical barrier",
        "framed by towering pillars",
        "reflecting the light of a thousand stars",
        "beckoning you forward",
    ]

    ending_phrases = [
        "You feel a sense of completion.",
        "You take a moment to savor your success.",
        "You breathe a sigh of relief.",
        "You step forward, eager for your next adventure.",
        "You can't help but smile at your accomplishment.",
        "Your heart swells with pride.",
        "You exit, ready for whatever comes next.",
    ]

    surrounding = random.choice(surroundings)
    atmosphere = random.choice(atmospheres)
    adj = random.choice(adjectives)
    phrase = random.choice(phrases)
    ending = random.choice(ending_phrases)

    description = (
        f"You've reached the exit, a {adj} passage leading to {surrounding}. "
        f"The atmosphere is filled with {atmosphere}. "
        f"The exit is {phrase}. {ending}"
    )

    return description


#assign description to room
room_desc = {}
monster_rooms = {}
def assign_description_to_rooms(game_map):
    global generate_random_monster_count
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == 0:
                room_description = generate_empty_room_description()
                room_desc[f'[{i}, {j}]'] = room_description
            elif game_map[i][j] == 1:
                room_description = generate_treasure_room_description()
                room_desc[f'[{i}, {j}]'] = room_description
            elif game_map[i][j] == 2:
                monster, generate_random_monster_count = generate_random_monster(generate_random_monster_count)
                room_description, monster_id = generate_monster_room_description(monster)
                room_desc[f'[{i}, {j}]'] = room_description
                monster_rooms[f'[{i}, {j}]'] = {'monster_id': monster_id}
            elif game_map[i][j] == 3:
                boss = generate_random_boss()
                room_description = generate_boss_room_description(boss)
                room_desc[f'[{i}, {j}]'] = room_description
            elif game_map[i][j] == 4:
                shopkeeper = generate_random_shopkeeper()
                item = generate_random_item()
                room_description = generate_shop_room_description(shopkeeper, item)
                room_desc[f'[{i}, {j}]'] = room_description
            elif game_map[i][j] == 5:
                room_description = generate_entrance_room_description()
                room_desc[f'[{i}, {j}]'] = room_description
            elif game_map[i][j] == 6:
                room_description = generate_exit_room_description()
                room_desc[f'[{i}, {j}]'] = room_description
    return room_desc, monster_rooms

def look(player_loc, room_desc):
    message = room_desc[str(player_loc)]
    print(create_textbox(message))

def create_textbox(text, max_width=180):
    lines = []
    for line in textwrap.wrap(text, max_width):
        padding = " " * (max_width - len(line))
        lines.append(f"| {line}{padding} |")
    text_height = len(lines)
    width = max_width + 4
    horizontal_line = "+" + "-" * (width - 2) + "+"
    vertical_line = "|" + " " * (width - 2) + "|"
    textbox = f"{horizontal_line}\n{vertical_line}\n" + "\n".join(lines) + f"\n{vertical_line}\n{horizontal_line}"
    return textbox

def initialize_money():
    money = 0
    bank = 0
    bank_int = 0.005
    return money, bank, bank_int

def print_money(money, bank, bank_int):
    return (f"Money: ${round(money, 2)}\nBank: ${round(bank, 2)}\nBank Interest: {bank_int * 100}%")

def add_money(money, amount):
    if admin == 1:
        money += int(amount)
        return money

def initialize_stats():
    player = {
        "name": "",
        "health": 100,
        "attack": 10,
        "defense": 10,
        "speed": 10,
        "luck": 10,
        "inventory": [],
        "equipped": [],
    }
    return player

def generate_monster_stats():
    monster = {
        "name": "",
        "health": 0,
        "attack": 0,
        "defense": 0,
        "speed": 0,
        "luck": 0,
        "inventory": [],
        "equipped": [],
    }





def generate_random_monster_stats(monster_rooms):

    monster_out = {}
    # Define the stats range for each monster
    monster_stats_range = {
        "vicious werewolf": {"health": (60, 100), "attack": (15, 25), "defense": (10, 15), "speed": (20, 30), "luck": (10, 20)},
        "bloodthirsty vampire": {"health": (80, 120), "attack": (20, 30), "defense": (15, 20), "speed": (10, 20), "luck": (10, 20)},
        "ferocious dragon": {"health": (150, 200), "attack": (30, 40), "defense": (20, 25), "speed": (5, 15), "luck": (5, 15)},
        "sinister ghost": {"health": (50, 80), "attack": (10, 20), "defense": (5, 10), "speed": (20, 30), "luck": (20, 30)},
        "giant spider": {"health": (40, 60), "attack": (20, 30), "defense": (5, 10), "speed": (40, 50), "luck": (10, 20)},
        "slime creature": {"health": (100, 150), "attack": (15, 25), "defense": (20, 25), "speed": (5, 10), "luck": (20, 30)},
        "skeleton warrior": {"health": (80, 120), "attack": (20, 30), "defense": (15, 20), "speed": (10, 20), "luck": (10, 20)}
    }

    # Define the abilities for each monster
    monster_abilities = {
        "vicious werewolf": "Rage",
        "bloodthirsty vampire": "Life Steal",
        "ferocious dragon": "Fire Breath",
        "sinister ghost": "Invisibility",
        "giant spider": "Web Shot",
        "slime creature": "Regeneration",
        "skeleton warrior": "Undead Resilience"
    }

    # Select a monster from the dictionary
    for coord in monster_rooms:
        monster_name = monster_rooms[coord]['monster_id'][:-1]
        monster_id = monster_rooms[coord]['monster_id']
        # Generate random stats within the monster's range
        monster_stats = {}
        for stat, stat_range in monster_stats_range[monster_name].items():
            monster_stats[stat] = random.randint(stat_range[0], stat_range[1])

        # Add the monster's ability
        monster_ability = monster_abilities[monster_name]

        # Return the monster with its stats and ability
        monster = {
            "name": monster_name,
            "stats": monster_stats,
            "ability": monster_ability,
            "monster_id": monster_id
        }
        monster_out[coord] = monster
    return monster_out

def generate_actions():
    ...

def interest(bank, bank_int):
    bank *= (bank_int + 1)
    return bank

def deposit(money, bank):
    bank += money
    money = 0
    return money, bank

def test_actions(player_loc, game_map, room_desc, bank_int):
    action_event(player_loc, game_map, room_desc, "f", bank_int)
    look(player_loc, room_desc)
    action_event(player_loc, game_map, room_desc, "b", bank_int)
    look(player_loc, room_desc)
    action_event(player_loc, game_map, room_desc, "r", bank_int)
    look(player_loc, room_desc)
    action_event(player_loc, game_map, room_desc, "l", bank_int)
    look(player_loc, room_desc)


def combat(monster, player):
    global admin, money, bank, bank_int, death
    monster = monster_out[str(player_loc)]
    print(create_textbox(f"You have encountered a {monster['name']}!"))
    while True:
        wait = time.sleep(3)
        player_stats = f'Health: {player["health"]}, Attack: {player["attack"]}, Defense: {player["defense"]}, Speed: {player["speed"]}, Luck: {player["luck"]}'
        monster_stats = f'Health: {monster["stats"]["health"]}, Attack: {monster["stats"]["attack"]}, Defense: {monster["stats"]["defense"]}, Speed: {monster["stats"]["speed"]}, Luck: {monster["stats"]["luck"]}'
        print(create_textbox(f"Your stats: {player_stats}"))
        print(create_textbox(f"{monster['name']}'s stats: {monster_stats}"))
        wait
        #print(f"{monster['name']}'s ability: {monster['ability']}")
        if player['speed'] > monster['stats']['speed']:
            print(create_textbox(f"You are faster than the {monster['name']}!"))
            print(create_textbox(f"What would you like to do?"))
            action = input(">>> ")
            if action == "attack":
                print(create_textbox(f"You attack the {monster['name']}!"))
                monster['stats']['health'] -= player['attack']
                wait
                if monster['stats']['health'] <= 0:
                    print(create_textbox(f"You have defeated the {monster['name']}!"))
                    print(create_textbox(f"You have earned ${monster['stats']['health'] * 2}!"))
                    money += monster['stats']['health'] * 2
                    return money, bank, bank_int
                print(create_textbox(f"The {monster['name']} attacks you!"))
                player['health'] -= monster['stats']['attack']
                wait
                if player['health'] <= 0:
                    print(create_textbox(f"You have been defeated by the {monster['name']}!"))
                    death = 1
                    return death
            elif action == "stats":
                print(create_textbox(f"Your stats: {player_stats}"))
                print(create_textbox(f"{monster['name']}'s stats: {monster_stats}"))
            elif action == "run":
                if random.randint(1, 100) <= player['luck']:
                    print(create_textbox(f"You run away from the {monster['name']}!"))
                    return money, bank, bank_int
                else:
                    print(create_textbox(f"You failed to run away from the {monster['name']}!"))
                    wait
                    print(create_textbox(f"The {monster['name']} attacks you!"))
                    player['health'] -= monster['stats']['attack']
                    wait
                    if player['health'] <= 0:
                        print(create_textbox(f"You have been defeated by the {monster['name']}!"))
                        return death
        else:
            wait
            print(create_textbox(f"The {monster['name']} is faster than you!"))
            print(create_textbox(f"The {monster['name']} attacks you!"))
            player['health'] -= monster['stats']['attack']
            wait
            if player['health'] <= 0:
                print(create_textbox(f"You have been defeated by the {monster['name']}!"))
                return death
            print(create_textbox(f"What would you like to do?"))
            action = input(">>> ")
            if action == "attack":
                print(create_textbox(f"You attack the {monster['name']}!"))
                monster['stats']['health'] -= player['attack']
                wait
                if monster['stats']['health'] <= 0:
                    print(create_textbox(f"You have defeated the {monster['name']}!"))
                    print(create_textbox(f"You have earned ${monster['stats']['health'] * 2}!"))
                    money += monster['stats']['health'] * 2
                    return money, bank, bank_int


def action_event(player_loc, game_map, room_desc, action, bank_int):
        global money, bank
        if action == "help":
            help()
        elif action == "quit":
            return
        elif action == "map":
            print_map(game_map, player_loc)
        elif action == "forward" or action == "backward" or action == "left" or action == "right" or action == "f" or action == "b" or action == "l" or action == "r":
            player_loc = move_player(action, player_loc, game_map, old_display_loc)
        elif action == "look":
            look(player_loc, room_desc)
        elif action == "money":
            print(create_textbox(print_money(money, bank, bank_int)))
        elif action.split()[0] == "add":
            money = add_money(money, action.split()[1])
        elif action == "deposit":
            money, bank = deposit(money, bank)
        elif action == "test":
            test_actions(player_loc, game_map, room_desc, bank_int)
        elif action == "monster":
            print(generate_random_monster_stats(monster_rooms))
        elif action == "combat":
            #try:
            combat(monster_out[str(player_loc)], player)
            #except:
                #print(create_textbox("There is no monster here!"))



game_map, player_loc, money, bank, bank_int, player, room_desc, monster_rooms, monster_out = start_game()


while True:
    display_loc = f'[{player_loc[1]}, {player_loc[0]}]'
    action = input("What would you like to do? ")
    action_event(player_loc, game_map, room_desc, action, bank_int)
    if death == 1:
        break
    old_player_loc = player_loc
    old_display_loc = f'[{old_player_loc[1]}, {old_player_loc[0]}]'
    bank = interest(bank, bank_int)

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
