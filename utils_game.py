import random
import math

resultStr = {
    "win": 'Вы угадали! Это число {}.',
    "fail": "Вы проиграли! Загаданное число: {}.",
    "startInfo":"Здесь отображаются результаты вашей попытки!",
    "pastMore": 'Загаданное число больше {0}. Количество оставшихся попыток: {1}.',
    "pastLess": 'Загаданное число меньше {0}. Количество оставшихся попыток: {1}.'
}

def generateRandomNumber(start, finish):
    return random.randint(start, finish)

def logarithmCountAttempts(start, finish):
    return math.ceil(math.log2(finish - start + 1))

def createGame(gameState):
    
    gameState["startNumber"] = generateRandomNumber(1, 500)
    startNum = gameState["startNumber"]

    gameState["finishNumber"] = generateRandomNumber(startNum + 1, 1000)
    finNum = gameState["finishNumber"]

    gameState["guessComputerNumber"] = generateRandomNumber(startNum, finNum)
    gameState["attemptsStart"] = logarithmCountAttempts(startNum, finNum)
    gameState["currentAttempts"] = gameState["attemptsStart"]
    gameState["resStr"] = resultStr["startInfo"]
    gameState["isGaming"] = True

def processGame(gameState, userGuessNum):

    userNum = int(userGuessNum)
    compNum = int(gameState["guessComputerNumber"])

    isWin = False
    if userNum > compNum:
        gameState["resStr"] = resultStr["pastLess"]
    elif userNum < compNum:
        gameState["resStr"] = resultStr["pastMore"]
    else:
        gameState["resStr"] = resultStr["win"].format(userNum)
        isWin = True
        gameState["isGaming"] = False

    gameState["currentAttempts"] = int(gameState["currentAttempts"]) - 1

    if gameState["currentAttempts"] == 0 and not isWin:
        gameState["resStr"] = resultStr["fail"].format(compNum)
        gameState["isGaming"] = False
    else:
        gameState["resStr"] = gameState["resStr"].format(userNum, gameState["currentAttempts"])