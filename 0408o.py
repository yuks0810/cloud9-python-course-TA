# Anaconda

# pythonの妖精
# 主体


def test1(n):
      print('test1 start', n)
      print('test1 end', n)
      return
      

def test2(n):
      print('test2 start', n)
      test1(n-1)
      print('test2 end', n)
      return

def test3(n):
      print('test3 start', n)
      test2(n-1)
      print('test3 end', n)
      return

def test4(n):
      print('test4 start', n)
      test3(n-1)
      print('test4 end', n)
      return

print('start')
test4(10)
print('end')
exit()


print('start1')

def test(a, b):
      print('test', a, b) # a:100, b:10
      c = a + b # 110
      return c
      
print('start2')

m = 100
n = 10
test(m, n)
x = test(m, n)

print('end', x)