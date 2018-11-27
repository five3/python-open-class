# f = open('test.xml', 'r')
# print type(f)
# f.close()
# # f = open('/Users/michael/notfound.txt', 'r')
#
# f = open('test.xml', 'r')
# print f.read(10)
#
# for line in f.readlines():
#     print(line.strip())
# f.close()
#
#
# try:
#     f = open('test.xml', 'r')
#     print f.read()
#     print type(f.read())
# finally:
#     if f:
#         f.close()
#
# with open('test.xml', 'r') as f:
#     print f.readline()


class Sample:
    def __enter__(self):
        print("In__enter__()")
        return "HuiCe"

    def __exit__(self, type, value, trace):
        print("In__exit__()")

def get_sample():
    return Sample()

with get_sample() as s:
    print("sample:", s)

