

# The Elf would first like to know which games would have been possible if the
# bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
possible = {'red': 12, 'green': 13, 'blue': 14}

possible_groups = []
def check_subset(data, maxsolution):
    data = data.strip(' ')
    for cubes in data.split(','):
        cubes = cubes.strip(' ')
        tmp = cubes.split(' ')
        count = int(tmp[0])
        color = tmp[1]
        if count > maxsolution[color]:
            return(False)
    return(True)

#with open('day02/input_example') as f:
with open('day02/input') as f:
    for line in f.readlines():
        line = line.rstrip()
        # print(line)
        tmp = line.split(':')
        game = tmp[0].split(' ')[1]
        data = tmp[1].split(';')
        game_possible = True
        for subset in data:
            if not check_subset(subset, possible):
                game_possible = False
        if game_possible:
            possible_groups.append(int(game))


#print(possible_groups)
#print(sum(possible_groups))

# part 2

game_powers = []

# with open('day02/input_example') as f:
with open('day02/input') as f:
    for line in f.readlines():
        line = line.rstrip()
        # print(line)
        tmp = line.split(':')
        game = tmp[0].split(' ')[1]
        data = tmp[1].split(';')
        min_set = {'red': 0, 'green': 0, 'blue': 0}
        for subset in data:
            # print(subset)
            subset = subset.strip(' ')
            for cubes in subset.split(','):
                cubes = cubes.strip(' ')
                tmp = cubes.split(' ')
                count = int(tmp[0])
                color = tmp[1]
                if min_set[color] < count:
                    min_set[color] = count
        power = min_set['red'] * min_set['green'] * min_set['blue'] 
        game_powers.append(power)

print(game_powers)
print(sum(game_powers))
