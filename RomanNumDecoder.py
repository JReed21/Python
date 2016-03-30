def solution(roman):
  add = 0
  lt5 = []
  rom = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
  y = list(roman)
  for x in y: 
      if not lt5:
          lt5.append(rom[x])
      else:
          if(lt5[0] < rom[x]):
              add += ((rom[x] - (lt5[0] * len(lt5))))
              lt5 = []
          else:
              lt5.append(rom[x])
  if(lt5):
      for x in lt5:
          add += x
  return add
              