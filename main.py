#oops (Object Oriented Programming Structure ) 88

class Student():
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.intro = ""

    def showDetails(self):
        print("The details of the students are ")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Hobby:",self.hobby)

    def introStudent(self):
        self.intro = input(">")
        print(self.intro)

#Object
s1 = Student("Anaadi", 13, "Chess")
s1.showDetails()
s1.introStudent()

s2 = Student("Mira", 14, "Sports")
s2.showDetails()
s2.introStudent()
