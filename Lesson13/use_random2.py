import random

nums = list(range(5))

print(random.choice(nums))
print(random.choices(nums, k = 3))
print(random.sample(nums, 3))

print(nums)
random.shuffle(nums)
print(nums)
