from dogs import Dog, English_Dog, Japanese_Dog

Dog.description()

dog = Dog("犬")
print(dog.name)
dog.bark()

English_Dog.description()

buddy = English_Dog()
print(buddy.name)
buddy.bark()

jake = English_Dog("Jake")
print(jake.name)
jake.bark()

Japanese_Dog.description()

pochi = Japanese_Dog()
print(pochi.name)
pochi.bark()

shiro = Japanese_Dog("シロ")
print(shiro.name)
shiro.bark()