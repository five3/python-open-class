class Student():

    school = 'huice'
    __expenses = '8800'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def print_score(self):
        print('%s: %d in %s' % (self.name, self.get_score(), Student.get_school()))

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def get_expenses():
        return Student.__expenses

std1 = Student('liuze', 18)
std1.set_score(90)
std1.print_score()
print(Student.get_expenses())

