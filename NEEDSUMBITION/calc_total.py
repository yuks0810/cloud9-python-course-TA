price_notax= int(input("税抜き価格を入力してください："))
price_tax = int(price_notax*1.08)

if price_tax >= 2000:
    print("送料は無料です")
    print('送料込みの値段は',price_tax,"です。")

else:
    print("送料として350円かかります")
    print("送料込みの価格は",price_tax + 350,"円です。")