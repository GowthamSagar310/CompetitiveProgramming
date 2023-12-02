import re 

f = open("input.txt" ,'r')
games = [line.strip() for line in f.readlines()]
r_max, g_max, b_max = 12, 13, 14
possible_games = []
patterns = [r'(\d+) red', r'(\d+) green', r'(\d+) blue']

def possible_count(r,g,b):
    if r > r_max or g > g_max or b > b_max:
        return False
    return True

def possible_game(game):
    configs = game.split(":")[1].split(";")
    r,g,b = 0,0,0
    for config in configs:
        if re.search(patterns[0], config):
            r = int(re.search(patterns[0], config).group(1))
        if re.search(patterns[1], config):
            g = int(re.search(patterns[1], config).group(1))
        if re.search(patterns[2], config):
            b = int(re.search(patterns[2], config).group(1))
        if not possible_count(r,g,b): return False
    return True

for id in range(len(games)):
    game = games[id]
    if possible_game(game):
        possible_games.append(id+1)

print(sum(possible_games))

# part 2 

def get_minimum_count(game):
    configs = game.split(":")[1].split(";")
    r,g,b = 0,0,0
    for config in configs:
        if re.search(patterns[0], config):
            r = max(r, int(re.search(patterns[0], config).group(1)))
        if re.search(patterns[1], config):
            g = max(g, int(re.search(patterns[1], config).group(1)))
        if re.search(patterns[2], config):
            b = max(b, int(re.search(patterns[2], config).group(1)))
    return r*g*b

min_count = 0
for id in range(len(games)):
    game = games[id]
    min_count += get_minimum_count(game)
print(min_count)