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

    def __str__(self):
       return 'Student name:%s age:%d' %(self.name, self.age)

    __repr__ = __str__

    def __getattr__(self, item):
        return 'unknown'

std1 = Student('xiaoming', 20)
print(std1.sex)
