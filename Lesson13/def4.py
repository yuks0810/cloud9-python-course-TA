def calc_bmi(height, weight):
    ret = weight / height ** 2
    return ret

height = float(input("身長(m)を入力："))
weight = float(input("体重(kg)を入力："))

bmi = calc_bmi(height, weight)
print(f"BMI値：{bmi:.1f}")