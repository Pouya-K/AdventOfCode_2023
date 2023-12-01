with open("day1.txt", 'r') as file:
    data = file.read().splitlines()


def part1():
    totalSum = 0
    for string in data:
        number = findSum(string)
        totalSum += int(number)
    print("Part 1 Answer: " + str(totalSum))


def findSum(string):
    number = ""
    for letter in string:
        if 48 <= ord(letter) <= 57:
            number = letter
            break
    for letter in string[::-1]:
        if 48 <= ord(letter) <= 57:
            number = number + letter
            break
    return number


def part2():
    totalSum = 0
    for x in range(len(data)):
        data[x] = data[x].replace("e", "ee")
        data[x] = data[x].replace("t", "tt")
        data[x] = data[x].replace("o", "oo")
        data[x] = data[x].replace("one", "1")
        data[x] = data[x].replace("two", "2")
        data[x] = data[x].replace("three", "3")
        data[x] = data[x].replace("foour", "4")
        data[x] = data[x].replace("five", "5")
        data[x] = data[x].replace("six", "6")
        data[x] = data[x].replace("seeveen", "7")
        data[x] = data[x].replace("eight", "8")
        data[x] = data[x].replace("nine", "9")
        number = findSum(data[x])
        totalSum += int(number)
    print("Part 2 answer: " + str(totalSum))


part1()
part2()
