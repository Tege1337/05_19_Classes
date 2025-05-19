class Student:
    name = ""
    age = 0
    sex = ""
    score = 0

tivadar = Student()
print(tivadar)

tivadar.name = "El Tivadar"
tivadar.age = 16
tivadar.sex = "Attack Helicopter"
tivadar.score = 20

print(f"\nNév: {tivadar.name} \nKor: {tivadar.age} \nPontszám: {tivadar.score}")