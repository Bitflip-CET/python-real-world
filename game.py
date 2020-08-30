import random
# Board Creation
board = [[0, 1, 2], 
         [3, 4, 5], 
         [6, 7, 8]]

def printBoard():
  print("\n")
  for row in board:
    print(*row)
  print("\n")

# Win Check
def winCheck(symbol):
  # Rows
  for row in range(3):
    if(board[row][0] == symbol and board[row][1] == symbol and board[row][2] == symbol):
      # print("Row", row)
      return True
  # Columns
  for column in range(3):
    if(board[0][column] == symbol and board[1][column] == symbol and board[2][column] == symbol):
      # print("Column", column)
      return True
  # Diagonals
  if(board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol):
    # print("Leading Diagonal")
    return True

  if(board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol):
    # print("Off Diagonal")
    return True

  return False

def main():
  turns = 9
  isPlayer = True
  choice = ''
  choices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
  while turns > 0:
    # If Player, Take input.
    if(isPlayer):
      symbol=playerSymbol
      printBoard()
      print(choices)
      choice = int(input("Enter your choice: "))
      if(choice not in choices):
        print("INVALID CHOICE!")
        continue
    else:
      symbol=AISymbol
      choice = random.choice(choices)
      print("AI Plays", choice)
    
    choices.remove(choice)
    # 0 -> 0, 0
    # 1 -> 0, 1
    # 2 -> 0, 2
    # 3 -> 0, 3
    # 5 -> 1, 1
    # 7 -> 2, 1 => 3 * 2 + 1
    # choice = 7

    column = choice % 3
    row = (choice - column)//3

    board[row][column] = symbol

    didPlayerWin = winCheck(playerSymbol)
    didAIWin = winCheck(AISymbol)

    if(didPlayerWin):
      printBoard()
      print("YOU WON!")
      break
    
    if(didAIWin):
      printBoard()
      print("YOU LOST!")
      break

    isPlayer = not isPlayer
    turns -= 1

    if(turns == 0):
      printBoard()
      print("DRAW!")

playerSymbol = input("What should be your Symbol: ")
AISymbol = input("What should be AI Symbol: ")

main()