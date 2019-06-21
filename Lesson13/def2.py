def introduce(name = "N/A", age = "??"):
    print("Hello!")
    print(f"My name is {name}.")
    print(f"I'm {age} years old.")

introduce("tanaka", 25)  # 引数を全て指定
introduce("suzuki")      # age を省略
introduce(age = 30)      # name を省略
introduce()              # name も age も省略