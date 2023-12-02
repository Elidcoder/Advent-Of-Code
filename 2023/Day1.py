# Reading the input
day1Input = open("Day_1.txt").read()
day1SplitInput = day1Input.split("\n")

# Functions to be used for part 2
def tryFindIntLeft(line):
  for index in [x + 1 for x in range(len(line))]:
    replacedLine = tryReplace(line[:index])
    if any(didgit.isdigit() for didgit in replacedLine):
      return next(filter(lambda x: x.isdigit(), replacedLine))
  raise(ValueError("No found numbers in: " + line))

def tryFindIntRight(line):
  for index in [x + 1 for x in range(len(line))]:
    replacedLine = tryReplace(line[-index:])
    if any(didgit.isdigit() for didgit in replacedLine):
      return next(filter(lambda x: x.isdigit(), replacedLine))
  raise(ValueError("No found numbers in: " + line))

def replaceWordWithNumber(line):
  leftMostNumber = tryFindIntLeft(line)
  rightMostNumber = tryFindIntRight(line)
  return int(leftMostNumber + rightMostNumber)

def tryReplace(line):
  return line.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace(
      "six", "6").replace("seven", "7").replace("eight", "8").replace(
          "nine", "9")

# Define both parts
def part1():
  onlyDidgits = [[y for y in x if y.isdigit()] for x in day1SplitInput]
  combinedFirstLastDidgits = [int(x[0] + x[-1]) for x in onlyDidgits]
  return sum(combinedFirstLastDidgits)
def part2():
  combinedFirstLastDidgits = list(map(replaceWordWithNumber, day1SplitInput))
  return sum(combinedFirstLastDidgits)

# Output the results
print("Part 1: " + str(part1()))
print("Part 2: " + str(part2()))
