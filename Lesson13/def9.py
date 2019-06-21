from health import bmi as b

height = float(input("身長を入力してください："))
weight = float(input("体重を入力してください："))

my_bmi = b(height, weight)

print(f"BMI値：{my_bmi:.1f}")
