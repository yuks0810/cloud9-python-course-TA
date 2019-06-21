# 九九のリストを作成する
list_kuku = []

for x in range(1,10):
    list_inner = []
    
    for y in range(1,10):
        list_inner.append(x * y)
        
    list_kuku.append(list_inner)


# 九九の表を表示する
for v in list_kuku:
    for h in v:
        print(f"{(h):3d}", end = "")
    
    print("")