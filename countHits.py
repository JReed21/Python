import itertools
import math
import timeit
def count_hits_powterm(dig_list, pow_):
  tups = []
  powL = []
  powNum = []
  hit_sorted_values = []
  t = len(dig_list)
  for x in xrange(1,t + 1):
      tups.append(list(itertools.permutations(dig_list,x)))
  for x in tups:
      for l in x:
          powL.append(list(l))
  powL = [int(''.join(map(str,x))) for x in powL[1:]]
  count = 0
  ma = max(powL)
  t = int(math.sqrt(ma))
  for x in xrange(1,ma):
      if(x*x > ma):
          break
      else:
          powNum.append(pow(x,pow_))
  for m in xrange(1,200):
    for x in xrange(0,t):
      check = check_powers(powNum,x,m)
      #check =  sum_of_powers(x,pow_,m,ma)
      if(check > ma):
         break
      elif(check in powL):
         hit_sorted_values.append(check)
  hit_sorted_values = list(set(hit_sorted_values))
  hit_sorted_values.sort()
  return (len(hit_sorted_values), hit_sorted_values)
def check_powers(powL,x,m):
    return sum(powL[x:x+m]) 
print(count_hits_powterm([3,4,5,2,6,7,8,9],3))

#Step 1: We form all the possible numbers with these digits
#Step 2: We form an array with the terms of a power sequence up to the 
#        maximum generated number (all the power terms should be less or equal than this maximum number).
#Step3:  We will form all the possible sub arrays with contiguous perfect squares, calculating its corresponding sum of terms. 
#        We start with sub-arrays with length 1, up to the maximum possible lengths.