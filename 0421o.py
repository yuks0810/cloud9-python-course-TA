L = [1, 2, 3, 4, 1, 3, 4, 1]

N = len(L)

D = {}

for n in L: # n:1
      if n in D:
            D[n] += 1
            
      else:
            D[n] = 1 #D : {1:3, 2:1, 3:2, 4:2}
print(D) #
exit()


D = {}
D['test'] = 1000
k = 'test'

if k in D:
      print('yes', D[k])
else:
      print('no')


exit()

L = [1, 2, 3, 4, 1, 3, 4, 1]

N = len(L)

D = {}

for i in range(N): # i:1
      n = L[i]     # n:2
      D[n] = i

print(D) # {2:1, 3:5, 4:6, 1:7}

exit()

D = {}
D['test'] = 1000
D['test2'] = 1001
D['test'] = 1002
print(D['test2'])
print(D)


exit()


# ローカル変数
# グローバル変数（モジュール変数）
#見ることができる
print('start1')
def test(a, b):
      D = a*2
      print('test', a, b, D)
      c = a + b + D
      return c
print('start2')

m = 10
n = 100
D = 1000
x = test(m, n)
print(D)


print('end', x)

