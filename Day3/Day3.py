with open("day3.txt", 'r') as file:
    data = file.read().splitlines()
totalSum = 0
temps = []


def addSum(x, y):
    global totalSum
    startNum, endNum = 0, len(data[x])
    for z in range(y - 1, -1, -1):
        if not data[x][z].isnumeric():
            startNum = z + 1
            break
    for z in range(y + 1, len(data[x])):
        if not (data[x][z].isnumeric()):
            endNum = z
            break
    totalSum += int(data[x][startNum:endNum])
    return endNum


def addSum2(x, y, temp):
    global totalSum
    startNum, endNum = 0, len(data[x])
    for z in range(y - 1, -1, -1):
        if not data[x][z].isnumeric():
            startNum = z + 1
            break
    for z in range(y + 1, len(data[x])):
        if not (data[x][z].isnumeric()):
            endNum = z
            break
    if not (data[x][startNum:endNum] in temp):
        temp.append(data[x][startNum:endNum])


def isSpecialCharacter(x, y):
    return data[x][y] != "." and not (data[x][y].isnumeric())


def nextToSpecial(x, i):
    nextTo = False
    if x != 0:
        nextTo = nextTo or isSpecialCharacter(x - 1, i)
        if i != 0:
            nextTo = nextTo or isSpecialCharacter(x - 1, i - 1)
        if i != len(data[x]) - 1:
            nextTo = nextTo or isSpecialCharacter(x - 1, i + 1)
    if x != len(data) - 1:
        nextTo = nextTo or isSpecialCharacter(x + 1, i)
        if i != 0:
            nextTo = nextTo or isSpecialCharacter(x + 1, i - 1)
        if i != len(data[x]) - 1:
            nextTo = nextTo or isSpecialCharacter(x + 1, i + 1)
    if i != 0:
        nextTo = nextTo or isSpecialCharacter(x, i - 1)
    if i != len(data[x]) - 1:
        nextTo = nextTo or isSpecialCharacter(x, i + 1)
    return nextTo


def part1():
    for x in range(len(data)):
        i = 0
        while True:
            if i == len(data[x]):
                break
            if data[x][i].isnumeric() and nextToSpecial(x, i):
                i = addSum(x, i) - 1
            i += 1
    print("Part 1 Answer: " + str(totalSum))

part2Sum = 0
for x in range(1, len(data) - 1):
    for y in range(1, len(data[x]) - 1):
        if data[x][y] == "*":
            tempArr = []
            if data[x-1][y].isnumeric():
                addSum2(x-1, y, tempArr)
            if data[x-1][y-1].isnumeric():
                addSum2(x-1, y-1, tempArr)
            if data[x-1][y+1].isnumeric():
                addSum2(x-1, y+1, tempArr)
            if data[x+1][y].isnumeric():
                addSum2(x+1, y, tempArr)
            if data[x+1][y-1].isnumeric():
                addSum2(x+1, y-1, tempArr)
            if data[x+1][y+1].isnumeric():
                addSum2(x+1, y+1, tempArr)
            if data[x][y - 1].isnumeric():
                addSum2(x, y-1, tempArr)
            if data[x][y + 1].isnumeric():
                addSum2(x, y+1, tempArr)
            if len(tempArr) == 2:
                part2Sum += int(tempArr[0]) * int(tempArr[1])
print("Part 2 Answer: " + str(part2Sum))
# part1()
