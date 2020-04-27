#Sudoku Solver Python
#Python 3.7
#Bhupinder Singh (MrChepe09)
#-------------------------------------------

#Solving Solution
def solve(bo):
  
  find = find_empty(bo)
  if not find:
    return True
  else:
    row, col = find

  for i in range(1, 10):
    if valid(bo, i, (row, col)):
      bo[row][col] = i

      if solve(bo):
        return True

      bo[row][col] = 0

  return False


#Checking for Valid Entry
def valid(bo, num, pos):
  #checking row
  for i in range(9):
    if(bo[pos[0]][i] == num and pos[1]!=i):
      return False

  #checking column
  for i in range(9):
    if(bo[i][pos[1]] == num and pos[0]!=i):
      return False

  #checking box
  box_x = pos[1] // 3
  box_y = pos[0] // 3
  for i in range(box_y*3, box_y*3 + 3):
    for j in range(box_x*3, box_x*3 + 3):
      if(bo[i][j]==num and (i, j) != pos):
        return False

  return True


#Printing Sudoku
def print_board(bo):
  for i in range(9):
    if(i%3==0 and i!=0):
      print("-------------------")
    for j in range(9):
      if(j%3==0 and j!=0):
        print("|", end='')

      if(j==8):
        print(bo[i][j])
      else:
        print(str(bo[i][j]) + " ", end="")


#Finding 0 in Board
def find_empty(bo):
  for i in range(9):
    for j in range(9):
      if(bo[i][j] == 0):
        return (i, j) #row, column

  return None

#Main Function
board = []
for i in range(9):
  a = list(map(int, input().split()))
  board.append(a)
print_board(board)
solve(board)
print("-----------------")
print()
print_board(board)
