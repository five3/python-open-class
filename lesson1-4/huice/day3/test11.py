class URL():

    def __init__(self, path='http://api.huice.server'):
        self.__path = path

    def __getattr__(self, path):
        return URL('%s/%s' % (self.__path, path))

    def __str__(self):
        return self.__path

print(URL().user.login)
