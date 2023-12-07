with open("day6.txt", 'r') as file:
    data = file.read().splitlines()
answer = 1
times = data[0][data[0].index(":") + 1:].split()
distances = data[1][data[1].index(":") + 1:].split()
for i in range(len(times)):
    eachTime = int(times[i])
    numOfWays = 0
    for x in range(1, eachTime):
        if x * (eachTime - x) > int(distances[i]):
            numOfWays += 1
    if numOfWays != 0:
        answer *= numOfWays
print("Part 1 Answer: " + str(answer))

numOfWays = 0
time = ""
distance = ""
for x in range(len(times)):
    time += times[x]
    distance += distances[x]
time = int(time)
distance = int(distance)
for x in range(1, time):
    if x * (time - x) > int(distance):
        numOfWays += 1
print("Part 2 Answer: " + str(numOfWays))