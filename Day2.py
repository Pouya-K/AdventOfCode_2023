with open("day2.txt", 'r') as file:
    data = file.read().splitlines()
totalSumPart1, totalSumPart2 = 0, 0
for line in data:
    line = line.replace(";", ",")
    numOfGreens, numOfBlues, numOfReds = 0,0,0
    gameNum = int((line.split()[1])[:len(line.split()[1])-1])
    games = line[line.index(":") + 2:].split(", ")
    for game in games:
        cube = game.split(" ")
        if cube[1][0] == 'r' and int(cube[0]) > numOfReds:
            numOfReds = int(cube[0])
        elif cube[1][0] == 'b' and int(cube[0]) > numOfBlues:
            numOfBlues = int(cube[0])
        elif cube[1][0] == 'g' and int(cube[0]) > numOfGreens:
            numOfGreens = int(cube[0])
    if numOfReds <= 12 and numOfGreens <= 13 and numOfBlues <= 14:
        totalSumPart1 += gameNum
    totalSumPart2 += numOfGreens*numOfReds*numOfBlues
print("Part 1 Answer: " + str(totalSumPart1))
print("Part 2 Answer: " + str(totalSumPart2))