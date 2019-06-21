import health

height = float(input("伸長を(m)入力してください："))
weight = float(input("体重(kg)を入力してください："))

my_bmi = health.bmi(height, weight)
my_standard_weight = health.standard_weight(height)

print(f"BMI値：{my_bmi:.1f}")
print(f"標準体重：{my_standard_weight:.1f}kg")