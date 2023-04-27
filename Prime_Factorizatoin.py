import math

def defFactor(n):
  if n < 2:
    print("Please enter the appropriate number")
  factor = 2
  lst = list()
  #n = None
  while factor <= n:
    if n % factor == 0:
      n = n/factor
      lst.append(n)
      #print(n)
      #print(lst)
    else:
      factor += 1
  print(lst)
defFactor(100)
