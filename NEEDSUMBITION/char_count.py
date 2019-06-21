#英単語を格納するための空のリスト
words = []

#アルファベット小文字の各文字をキーとして、値の初期値を0とした辞書
each_words = dict.fromkeys(list("abcdefghijklmnopqrstuvwxyz"), 0)

try:
      while True:
            val = input("英単語を入力してください：")
            if val == "":
                  break
      
            words.append(val)
            words.sort()
            
finally:
      print(("入力した単語：" + str(words)))
      
for w in words:
      for a in w:
            try:
                  each_words[a] += 1
            
      
            except KeyError:
                  pass
            
for k, v in each_words.items():
      if v < 1:
            pass
      else:
            print(f'{k}が{v}個ありました')