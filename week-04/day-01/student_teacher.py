''' Create Student and Teacher classes
- Student
  - learn()
  - question(teacher) -> calls the teachers answer method
- Teacher
  - teach(student) -> calls the students learn method
  - answer() '''

class Student(object):
    def learn(self):
        return "6 * 3 = 18"

    def question(self, teacher):
        return teacher.answer()

class Teacher(object):
    def teach(self, student):
        return student.learn()

    def answer(self):
        return "it's ok"

Lajos = Student()
Marika = Teacher()

print(Lajos.question(Marika))
print(Marika.teach(Lajos))