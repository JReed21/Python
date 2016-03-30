import itertools
def lcs(x, y):
  print(len(x),len(y))
  splitX = splitoff(x)
  splitY = splitoff(y)
  matrix = [[0 for xx in xrange(len(y))] for yy in range(len(x))]
  for i,k in enumerate(splitX):
      for j,l in enumerate(splitY):
           matrix[i][j] = len((set(k) & set(l)))
  i = len(x)-1
  j = len(y)-1
  returnThis = ""
  while(i >= 0 and j >= 0):
      if(x[i] == y[j]):
          returnThis += x[i]
          i = i - 1
          j = j - 1
      elif(i == 0):
          j = j - 1
      elif(j == 0):
          i = i - 1
      elif(matrix[i-1][j] > matrix[i][j-1]):
          i = i - 1
      else:
          j = j - 1
  return returnThis[::-1]
def splitoff(x):
  splitted = []
  count = 1
  while(count <= len(x)):
      splitted.append(x[0:count])
      count = count + 1
  return splitted

import time

start_time = time.time()
print lcs("abcdefghijklmnopqrstuvwxyzabcdefghijkabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzlmabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwmnopqrstuvwxyzabcdefghijklmnopqrstumnopqrstuvwxyzabcdefghijklmnopqrstumnopqrstuvwxyzabcdefghijklmnopqrstumnopqrstuvwxyzabcdefghijklmnopqrstuxyznopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrsabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyztuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyzabcdefghijklabcdefghijklmnopqrstuvwxyzmnopqrstuvwxyzabcdefghiabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzjklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")

print("--- %s seconds ---" % (time.time() - start_time))
