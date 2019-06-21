

a = 0
print(a)
a += 1
print(a)
a += 10
print(a)
a += b
print(a)


exit()

i = 0
while i < 5:   # False
      print(i) # => 4
      i += 1   # i:5
print('end', i)
exit()


# ブロック構造(階層構造)

n = 18
if n % 5 == 0:
      print('yes1')
      if n % 3 == 0:
            print('yes2')
      else:
            print('no2')
      print('end1')
else:
      print('yes3')
      if n % 3 == 0:
            print('yes4')
      else:
            print('no4')
      print('end3')
print('end')