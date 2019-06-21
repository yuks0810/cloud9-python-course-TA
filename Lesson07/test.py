l = []

while True:
    val = int(input('点数を入力してください：'))
    if val == -1:
        break
    
    l.append(val)
sum = sum(l)
num = len(l)
    
average_score = sum / num


print(num,"人のテストの平均点は",average_score,"です。")