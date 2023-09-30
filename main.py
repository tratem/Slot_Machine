import random

TOTAL_DEPOSIT = 0
ROWS = 3
COLUMNS = 5
WIN3 = 5
WIN4 = 10
WIN5 = 20
JACKPOT = 900

def deposit():
    while True:
        amount = input("How much $ do you want to deposit? ")
        if amount.isdigit():
            amount = float(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0. Try again:")
        else:
            print("Please enter a number.")
    global TOTAL_DEPOSIT 
    TOTAL_DEPOSIT += float(amount)
    
    return amount

def bet(credits):
    while True:
        hand_value = input("Your total credit balance is: " + str(credits) + "\n" + "Please enter betting value in credits: ")
        if hand_value.isdigit():
            hand_value = float(hand_value)
            if hand_value >= 10:
                break
            else:
                print("The minimum bet is 10. Try different amount:")
        else:
            print("Please enter a number.")
    
    return hand_value

def game(hand):
    prize = 0
    matrix = []
    for i in range(ROWS):
        row = []  
        for j in range(COLUMNS):
            random_number = random.randint(1, 9)
            row.append(random_number)
        matrix.append(row)  
    
    #TESTING
    for i in range(ROWS):
        for j in range(COLUMNS): 
            print (matrix[i][j], end="")
        print ("")

    #JACKPOT
    element = matrix[0][0]
    for i in range(ROWS):
        for j in range(COLUMNS):  
            if element != matrix[i][j]:
                JP = False
                break
            else:
                JP = True
        if JP == False:
            break
    if JP == True:
        print ("CONGRATULATIONS! YOU WON THE JACKPOT!!!!")
        prize = hand * JACKPOT
        return prize
    
    #Row Winnings
    for i in range(ROWS): 
        #5 in a row
        for k in range(1, COLUMNS):
            if matrix[i][0] == matrix[i][k]:
                row5 = True
            else:
                row5 = False
                break
        if (row5 == True):
            prize += hand * WIN5
            if (i == ROWS - 1):
                return prize
            else:
                i += 1
        #4 and 3 in a row        
        for j in range(COLUMNS):
            #4 in a row
            if j < COLUMNS - 3 and (matrix[i][j] == matrix[i][j + 1] == matrix[i][j + 2] == matrix[i][j + 3]) :
                prize += hand * WIN4
            #3 in a row
            elif j < COLUMNS - 2 and (matrix[i][j] == matrix[i][j + 1] == matrix[i][j + 2]):
                prize += hand * WIN3
    
    #Column Winnings
    for j in range(COLUMNS):
        for i in range(ROWS):
            #3 in a column
            if matrix[0][j] == matrix[i][j]:
                col3 = True
            else:
                col3 = False
                break
        if col3 == True:
            prize += hand * WIN3
    return prize 
    
def main():
    credits = deposit() * 100
    hand = bet(credits)
    credits -= hand
    credits += game(hand) 
    
    while True:
        print ("Credits now: " + str(credits))
        user_input = input("Press Enter to continue, type 'q' to quit, type 'c' to add credits or type 'b' to change the betting value: ").upper()
        if user_input == '' and credits < hand:
            print("Sorry, you don have enough credits. Do you want to add more [C]redit, do you want to change the [B]et value, or do you want to [Q]uit the game")
            low_credit_input = input("").upper()
            if low_credit_input == 'C': #deposit
                credits += deposit() * 100
                continue
            elif low_credit_input == 'B': #change betting value
                hand = bet(credits)
                continue
            elif low_credit_input == 'Q': #cashout
                print("Cashing out. Thanks for playing")
                break
        elif user_input == '': #new round
            credits -= hand
            credits += game(hand)
            continue
        elif user_input == 'Q': #cashout
            print("Cashing out. Thanks for playing")
            break
        elif user_input == 'C': #deposit 
            credits += deposit() * 100
            continue
        elif user_input == 'B': #change betting value
            hand = bet(credits)
            continue
        
    
main()
