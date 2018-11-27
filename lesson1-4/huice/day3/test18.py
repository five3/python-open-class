import sys

print(type(sys.argv))
print(type(sys.argv[0]))

if len(sys.argv)>2:
    print('pass')
else:
    print('缺少参数')



# exit
def exitfunc(value):
    print(value)
    # sys.exit(0)

print("hello")

try:
    sys.exit(1)
except SystemExit as value:
    exitfunc(value)

print("come?")

# modules
print(sys.modules)

def dump(module):
    result = module + ' =>'
    if module in sys.builtin_module_names:
        result += ' <BUILTIN>'
    else:
        try:
            module = __import__(module)
            result += ' ' + module.__file__
        except:
            result += ' 模块名无效'
    return result

print(dump("os"))
print(dump("sys"))
print(dump("string"))
print(dump("json"))
print(dump("xml"))
print(dump("huice"))

