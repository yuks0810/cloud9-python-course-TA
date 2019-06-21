from health import bmi 

height = float(input("身長を入力してください："))
weight = float(input("体重を入力してください："))

my_bmi = bmi(height, weight)

print(f"BMI値:{my_bmi:.1f}")

