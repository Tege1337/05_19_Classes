class Student:
    name = ""
    age = 0
    sex = ""
    score = 0

    def introduce(self):
        print(f"\nNév: {self.name} \nKor: {self.age} \nPontszám: {self.score}")


    def study(self, point):
        self.score += point


tivadar = Student()
print(tivadar)

tivadar.name = "El Tivadar"
tivadar.age = 16
tivadar.sex = "Attack Helicopter"
tivadar.score = 20
tivadar.mood = "stressed"

tivadar.introduce()
tivadar.study(12)