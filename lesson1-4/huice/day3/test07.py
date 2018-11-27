std1 = { 'name': 'Liuze', 'score': 98 }
std2 = { 'name': 'Tiantian', 'score': 59 }

def print_score(std):
    print('%s: %s' % (std['name'], std['score']))

print_score(std1)


class Student():

    school = 'huice'
    __expenses = '8800'

    def __init__(self, name, score=0, age=18):
        self.name = name
        self.score = score
        self.__age = age

    def print_score(self):
        print('%s: %d' % (self.name, self.score))


std1 = Student('Liuze', 100)
std2 = Student('Tiantian', 59)


# std1.print_score()
# std2.print_score()
#
# print id(std1)
# print id(std2)
#
# std2.score = 100
# std2.print_score()
# Student('Zhangsan').print_score()

print(std1.school)
std1.school = '51'
print(std1.school)
print(std2.school)
Student.school = '51testing'
print(std1.school)
print(std2.school)

print(std1.expenses)
print(std1.age)
print(std1._Student__expenses)
print(std1._Student__age)





