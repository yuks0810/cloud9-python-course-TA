import health as h

height = float(input("身長を入力してください："))
weight = float(input("体重を入力してください："))

my_bmi = h.bmi(height, weight)
my_standard_weight = h.standard_weight(height)

print(f"BMI値：{my_bmi:.1f}")
print(f"標準体重・{my_standard_weight:.1f}kg")

