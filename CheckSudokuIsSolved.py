def done_or_not(board): #board[i][j]
  row = []
  col = []
  box = []
  if(len(board) != len(board[0])):
      return 'Try again!'
  for x in range(len(board)):
      for y in range(len(board[0])):
          if(y % 3 == 0):
              if box:
                  box = []
              for n in range(y,y+2):
                  for m in range(y,y+2):
                     if board[n][m] not in box:
                       box.append(board[n][m])
                     else:
                       return 'Try again!'
          if board[x][y] not in row:
              row.append(board[x][y])
          else:
              return 'Try again!'              
          if board[y][x] not in col:
              col.append(board[y][x])
          else:
              return 'Try again!'
      row = []
      col = []
  return 'Finished!'