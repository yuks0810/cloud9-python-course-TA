
import random

L = []
for i in range(30):
      n = random.randint(0, 100)
      L.append(n)
      
print(L)
# 内包表記
#L = [random.randint(0, 100) for i in range(30)]
#print(L)

answer = min(L)
print(answer)
#L.sort()
#answer = L[0]
#print(answer)


#宿題(Lから最小値のみをプリントする)
#for loop or while loop
if L[n]<L[n-1]:
      print(L[n-1])
      
else:
      print(L[n])

exit()

L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

print(L[1:3][1])
exit()



for a in L: # a:[1, 2, 3]
      for b in a: # b:3
            print(b) # => 3
      print()

exit()

print(L[1])

print(L[1][1])

#a = L[1] # a:[4, 5, 6]
#print(a[1])


exit()
L = [0, 'test', [1, 2, 3]]



exit()
L = [1, 3, 2, 4, 7, 5, 6, 8]

N = len(L)
L2 = []
for i in range(N): # i:0
      n = L[i]    
      if i == n:
            L2.append(n)
            
print(L2)



#print(L[4])
#L[0] = 100
#L[4] = 100
#L.append(100)
#print(L)
#n = len(L)
#print(n)
#print(L[1:3]) # L[0] L[1]
