sports = []

#　リストへ登録
while True:
      s = input('スポーツの名前を入力：')
      
      if s == "":
            break
      
      sports.append(s)
      
#リストから1件ずつ表示
for s in sports:
      print(s)
      
print("以上です")