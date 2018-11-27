import json

stu1 = {'name': 'xiaoming', 'age': 20, 'height': 170}
json_stu1 = json.dumps(stu1)
print(type(json_stu1), json_stu1)

stu2 = {1:'xiaoming', 2:20, 3:170}
json_stu2 = json.dumps(stu2)
print(type(json_stu2), json_stu2)

stu3 = {'name': 'xiaoming', 'age': 20, 'height': 170, 'fruits':['apple', 'banana']}
json_stu3 = json.dumps(stu3)
print(type(json_stu3), json_stu3)

stu4 = {'name': 'xiaoming', 'age': 20, 'height': 174.2, 'fruits':['apple', 'banana']}
json_stu4 = json.dumps(stu4)
print(type(json_stu4), json_stu4)

stu5 = {'name': 'xiaoming', 'age': 20, 'height': 174.2, 'is_married':True, 'sroce':None}
json_stu5 = json.dumps(stu5)
print(type(json_stu5), json_stu5)

stu6 = "{'name': 'xiaoming', 'age': 20, 'height': 174.2, 'is_married':True, 'sroce':None}"
stu6 = "{1.5: 'xiaoming', 'age': 20, 'height': 174.2, 'is_married':True, 'sroce':None}"
json_stu6 = json.dumps(stu6)
print(type(json_stu6), json_stu6)

stu7 = [['name','xiaoming'],['age',20],['height', 174.2]]
json_stu7 = json.dumps(stu7)
print(type(json_stu7), json_stu7)