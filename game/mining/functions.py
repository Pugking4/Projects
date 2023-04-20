from colored import fg, style
import random

dirt_col = fg(94)
coal_col = fg(0)
iron_col = fg(235)
tin_col = fg(255)
copper_col = fg(208)

green = fg(34)
brown = fg(215)
grey = fg(240)
reset = style.RESET

"""
Base Blocks:
dirt = # brown
stone = # grey

Common Blocks:
Iron = O grey
Coal = O black
Tin = O cyan
Copper = O yellow

Rare Blocks:


Layers 0 - 17:
70% Dirt
10% Coal
10% Iron
5% Tin
5% Copper

Layers 17 - 40:
"""

#random.seed()

dirt_float = 0.75
coal_float = 0.1
iron_float = 0.05
tin_float = 0.05
copper_float = 0.05

class gen:
    def mining_surface(map_size):
        game_map = []
        for y in range(map_size*2):
            row = []
            for x in range(map_size):
                if y == 0:
                    row.append(0)
                else:
                    row.append(random.random())
            game_map.append(row)

        for y in range(len(game_map)):
            for x in range(len(game_map[y])):
                if game_map[y][x] < dirt_float:
                    game_map[y][x] = dirt_col + "#" + reset
                elif game_map[y][x] < dirt_float + coal_float:
                    game_map[y][x] = coal_col + "O" + reset
                elif game_map[y][x] < dirt_float + coal_float + iron_float:
                    game_map[y][x] = iron_col + "O" + reset
                elif game_map[y][x] < dirt_float + coal_float + iron_float + tin_float:
                    game_map[y][x] = tin_col + "O" + reset
                elif game_map[y][x] < dirt_float + coal_float + iron_float + tin_float + copper_float:
                    game_map[y][x] = copper_col + "O" + reset

        return game_map
    
    def surface(map_size):
        surface_map = []
        row = []
        for i in range(map_size):
            if i == 4:
                row.append(green + '/\\' + reset)
            else:
                row.append(' ')
        surface_map.append(row)

        row = []
        for i in range(map_size):
            if i == 3:
                row.append(green + '/' + reset)
            elif i == 5:
                row.append(green + '\\' + reset)
            elif i == 4:
                row.append(green + '/\\' + reset)
            else:
                row.append(' ')
        surface_map.append(row)

        row = []
        for i in range(map_size):
            if i == 3:
                row.append(green + '//' + reset)
            elif i == 5:
                row.append(green + '\\\\' + reset)
            elif i == 4:
                row.append(green + '/\\' + reset)
            else:
                row.append(' ')
        surface_map.append(row)
        
        row = []
        for i in range(map_size):
            if i > 1 and i < 4:
                row.append(green + '//' + reset)
            elif i > 3 and i < 6:
                row.append(green + '\\\\' + reset)
            else:
                row.append(' ')
        surface_map.append(row)
        row = []
        for i in range(2):
            row = []
            for j in range(map_size):
                if j == 4:
                    row.append(brown + '||' + reset)
                else:
                    row.append(' ')
            surface_map.append(row)

        row = []
        for i in range(map_size):
            row.append(green + '#' + reset)
        surface_map.append(row)


        return surface_map

class player:
    def init_player():
        player_loc = [2, 5]
        return player_loc