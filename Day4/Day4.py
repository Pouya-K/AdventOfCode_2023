with open("day4.txt") as file:
    data = file.read().splitlines()
numOfCardsWon = 0


def part1():
    totalSum = 0
    for line in data:
        winningNumbers = line[line.index(":") + 2: line.index("|") - 1].split()
        yourNumbers = line[line.index("|") + 2:].split()
        winningNumsFound = 0
        for number in yourNumbers:
            if number in winningNumbers:
                winningNumsFound += 1
        if winningNumsFound > 0:
            totalSum += 2 ** (winningNumsFound - 1)
    print("Part 1 Answer: " + str(totalSum))


def winCard(index):
    global numOfCardsWon
    numOfCardsWon += 1
    line = data[index]
    winningNumbers = line[line.index(":") + 2: line.index("|") - 1].split()
    yourNumbers = line[line.index("|") + 2:].split()
    winningNumsFound = 0
    for number in yourNumbers:
        if number in winningNumbers:
            winningNumsFound += 1
    if winningNumsFound != 0:
        for i in range(1, winningNumsFound + 1):
            winCard(i + index)


def part2():
    for x in range(len(data)):
        winCard(x)
    print("Part 2 Answer: " + str(numOfCardsWon))


part1()
part2()