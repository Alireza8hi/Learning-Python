cs = [
    {
        "title": "python",
        "Teacher": "amiri"
    },
    {
        "title": "HTML",
        "Teacher": "alavi"
    },
    {
        "title": "PHP",
        "Teacher": "sadeghi"
    }
]


class User:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def introduce(self):
        print(self.name, self.lastname)


class Student(User):
    def __init__(self, name, lastname, email):
        super().__init__(name, lastname)
        self.email = email
        self.courses = []

    def introduce(self):
        print("I'm a student")
        super().introduce()
        print(self.email)

    def printcourses(self):
        if len(self.courses) == 0:
            print("there is no course")
        else:
            for course in self.courses:
                print(course["title"])


class Teacher(User):
    def __init__(self, name, lastname, code):
        super().__init__(name, lastname)
        self.code = code

    def introduce(self):
        print("I'm a teacher")
        super().introduce()
        print(self.code())


p1 = Teacher("ali", "zahedi", 213)
p2 = Student("narges", "miladi", "narges222@gmail.com")
print(p2.courses)
p2.courses.append(cs[1])
print(p2.courses)

p2.printcourses()
p2.courses.append(cs[0])
p2.printcourses()
p2.courses.clear()
p2.printcourses()
