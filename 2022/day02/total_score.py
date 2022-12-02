CHOICES = ["A", "B", "C", "X", "Y", "Z"]
ROCK = 0
PAPER = 1
SCISSORS = 2

beats = {ROCK: PAPER, PAPER: SCISSORS, SCISSORS: ROCK}
# <value> beats <key>
loses = {ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER}
# <value> loses to <key>


def getScore(opponentChoice, yourChoice):
    opponentChoice = CHOICES.index(opponentChoice) % 3
    yourChoice = CHOICES.index(yourChoice) % 3

    score = yourChoice + 1  # the number of points you get for chosing a certain shape to play
    if opponentChoice == yourChoice:
        return score + 3

    elif yourChoice == beats[opponentChoice]:
        return score + 6
    else:
        return score


def getNewScore(opponentChoice, yourCommand):
    opponentChoice = CHOICES.index(opponentChoice) % 3
    yourCommand = CHOICES.index(yourCommand) % 3

    # the number of points you get by being told to lose, draw, or win
    score = yourCommand * 3

    if yourCommand == 0:  # lose
        return score + loses[opponentChoice] + 1

    if yourCommand == 1:  # draw
        return score + opponentChoice + 1

    if yourCommand == 2:  # win
        return score + beats[opponentChoice] + 1


f = open("input.txt", "r")
totalScore = 0
for line in f:
    totalScore += getNewScore(line[0], line[2])

print(totalScore)
