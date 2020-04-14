def game():
    import sys
    import random

    print("********---******","PFS ticTacToe Game","**********---******")
    print("   **************","Have fun","*************************   ")

    #A function that takes both players names and their symbol respectively and change to uppercase
    def take_input():
        try:
            global player1
            global player1Sign
            global player2
            global player2Sign
            player1 = input("Player 1 enter your name\n").upper()
            player1Sign = str(input(f"{player1} choose the symbol you want 'X or O' or customize: ")).upper()
            player2 = input("Player 2 enter your name\n").upper()
            player2Sign = str(input(f"{player2} choose the symbol you want 'X or O' or customize: ")).upper()
            if ((player1.isspace()) or (player1Sign.isspace())) or ((player2.isspace()) or (player2Sign.isspace())):
                print("\n")
                print("Name or symbol can not be empty")
                print("Enter a valid name")
                take_input()
            if ((player1 == "") or (player1Sign == "")) or ((player2 == "") or (player2Sign == "")):
                print("\n")
                print("Name or symbol can not be empty")
                print("Enter a valid name")
                take_input()
            if (player1 == player2) or (player1Sign == player2Sign):
                print("\n\n")
                print("Both names are the same\nEnter different names")
                take_input()
        except Exception:
            take_input()
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            print("Enter 'exit' to quit")
            take_input()
    take_input()
    p1 = player1
    p2 = player2
    p1_score = 0
    p2_score = 0
    tie = 0
    print("\n")
    #Keep scores
    print(p1,p1_score,p2,p2_score,"Ties",tie)

    while True:
        #The TicTacToe game Layout
        playBoard = {"1":"1", "2":"2", "3":"3",
                "4":"4", "5":"5", "6":"6",
                "7":"7", "8":"8", "9":"9"
        }

        random_words = ["Nice move!", "Sharp thought!", "Good move!", "Better play!", "Hmm cool!", "That was good!"]

        #Function to print out the Tic Tac Toe game Layout
        def getBoard(board):
            print(board["1"],"|",board["2"],"|",board["3"])
            print("-----------")
            print(board["4"],"|",board["5"],"|",board["6"])
            print("-----------")
            print(board["7"],"|",board["8"],"|",board["9"])



        #Keep count of the input to stop taking input after 9 items
        count = []


        #Store players names and symbol in another variable
        sign = player1Sign
        p = player1

        pAndSignDict = {player1Sign:player1,player2Sign:player2}

        #Check if the input Matches the winning combination

        def checkWinnerSymbol(combo_value):
            val = random.choice(combo_value)
            if playBoard[val] in pAndSignDict.keys():
                global p_winner
                p_winner = pAndSignDict[playBoard[val]]
                sign = playBoard[val]
                getBoard(playBoard)

        def winCheck(board):
            global winCheck
            winCheckDict = {"1,5,9":(board["1"] == board["5"] == board["9"]),
                            "3,5,7":(board["3"] == board["5"] == board["7"]),
                            "4,5,6":(board["4"] == board["5"] == board["6"]),
                            "2,5,8":(board["2"] == board["5"] == board["8"]),
                            "1,4,7":(board["1"] == board["4"] == board["7"]),
                            "3,6,9":(board["3"] == board["6"] == board["9"]),
                            "1,2,3":(board["1"] == board["2"] == board["3"]),
                            "7,8,9":(board["7"] == board["8"] == board["9"])
            }
            key_value = list(winCheckDict.values())
            the_key = list(winCheckDict.keys())
            if True in key_value:
                get_value_index = key_value.index(True)
                get_key = the_key[get_value_index]
                combination_values = get_key.split(",")
                checkWinnerSymbol(combination_values)
                return True
            #Check if there is a draw
            if (key_value[0] and key_value[1] and key_value[2] and key_value[3] and key_value[4] and key_value[5] and key_value[6] and key_value[7]) == False:
                return False
        print("Enter exit to quit game")

        #Take input and Check if there is a winner then print the winner

        while True:
            try:
                print("\n")
                print(player1,"is",player1Sign,"while",player2,"is",player2Sign)
                print(p,"enter where to play",sign ,"\n")
                getBoard(playBoard)
                position = str(input())
                if position == "exit":
                    sys.exit()
                if position == playBoard[position]:
                    playBoard[position] = sign
                    if len(count) > 1:
                        print("\n")
                        print(random.choice(random_words))
                else:
                    print("Position is not valid")
                    print("Enter number into a vacant position")
                    continue

            except KeyboardInterrupt:
                print("Enter 'exit' to exit")
                continue

            except KeyError:
                print("Key Error input a valid key")
                continue

            if sign == player1Sign:
                sign = player2Sign
                p = player2
            else:
                sign = player1Sign
                p = player1
            count.append(position)

            if len(count) == 9:
                sign = player1Sign
                p = player1
                playBoard[position] = sign
                getBoard(playBoard)
                if winCheck(playBoard) == False:
                    break
                else:
                    pass
            if winCheck(playBoard) == True:
                winCheck(playBoard)
                print("\nGame Over\n")
                break
        #print and add score of the winner
        if winCheck(playBoard) == True:
            if p_winner == p1:
                p1_score = p1_score + 1
            elif p_winner == p2:
                p2_score = p2_score + 1
            print(p_winner,"wins")
        #print and add score of the draw
        elif winCheck(playBoard) == False:
            print("\nIt is a draw")
            tie = tie + 1

        print(p1,p1_score,p2,p2_score,"Ties",tie)

        def replay():
            playAgain = input("Do you want to play Again 'y' or 'n': ").upper()
            try:
                if playAgain == "Y":
                    return True
                elif playAgain == "N":
                    sys.exit()
                if playAgain != ("Y" or "N"):
                    print("Incorrect Input")
                    replay()
            except Exception:
                print("Enter Y or N")
                replay()
            except KeyboardInterrupt:
                print("Enter Y or N")
                replay()
        if replay() == True:
            continue

game()

















