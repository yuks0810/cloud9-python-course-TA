def fibo(x):
      if x == 0:
            return 0
      elif x == 1:
            return 1
      elif x == 2:
            return 1
      else:
            return fibo(x-2) + fibo(x-1)
            

