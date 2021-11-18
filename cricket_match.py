#Play Cricket Match With Python
import random 
game = True

# Funtion for the computer chasing the user's total
def computerChase(userScore):
    isComputerOut = False
    didComputerWin = False
    computerTotal = 0

    while isComputerOut != True and didComputerWin != True:
        userNumber = int(input('Enter number between 1 and 6: '))
        computerNumber = random.randint(1, 6)

        if userNumber == computerNumber:
            print('\nYou win !!!')
            print('Computer scored', str(computerTotal))
            print('You win by', str(userScore - computerTotal), 'runs\n')
            isComputerOut = True
            didComputerWin = True
        elif computerTotal >= userScore:
            computerTotal += computerNumber
            print('\nComputer Wins')
            print('Computer scored', str(computerTotal), 'runs\n')
            isComputerOut = True
            didComputerWin = True
        else:
            print('Computer score', str(computerNumber))
            computerTotal += computerNumber

# Function for the user chasing computer's total
def userChase(computerScore):
    userTotal = 0
    isPlayerOut = False
    didPLayerWin = False

    while isPlayerOut != True and didPLayerWin != True:
        userNumber = int(input('Enter number between 1 and 6: '))
        computerNumber = random.randint(1, 6)

        if userNumber == computerNumber:
            if (computerScore - userTotal) < 0:
                print('You win !!!\n')
            else:
                print('\nYou are out !!!')
                print('Computer win by', str(computerScore - userTotal), 'runs\n')
                isPlayerOut = True
                didPLayerWin = True
        elif userTotal >= computerScore:
            userTotal += userNumber
            print('\nYou win !!!')
            print('You scored', str(userTotal), '\n')
            didPLayerWin = True
            isPlayerOut = True
        else:
            userTotal += userNumber
            print('You score', str(userNumber))

# Function for the batting processs
def bat():
    userTotal = 0
    isPlayerOut = False

    while isPlayerOut != True:
        userNumber = int(input('Enter number between 1 and 6: '))
        computerNumber = random.randint(1, 6)

        if userNumber == computerNumber:
            print('\nYou are out !!!')
            print('You scored', str(userTotal))
            isPlayerOut = True
            print('It is time for the computer to score your target\n')
            computerChase(userTotal)
        else:
            print('You score', str(userNumber))
            userTotal += userNumber

# Function for the bowling process
def bowl():
    isComputerOut = False
    computerTotal = 0

    while isComputerOut != True:
        userNumber = int(input('Enter number between 1 and 6: '))
        computerNumber = random.randint(1, 6)

        if userNumber == computerNumber:
            print('\nComputer is out !!!')
            print('Computer scored', str(computerTotal))
            print('Now you have to reach computer\'s score', '\n')
            userChase(computerTotal)
            isComputerOut = True
        else:
            print('Computer scored', str(computerNumber))
            computerTotal += computerNumber

# Program Execution
while game == True:
    userChoice = int(input('What do you choose; 1.Bat, 2.Bowl, 3.Exit: '))
    if userChoice == 1:
        bat()
    elif userChoice == 3:
        exit()
    else:
        bowl()
    