data = {
    '李晨': {'语文': 60, '数学': 68, '英语': 45},
    '石宇': {'语文': 10, '数学': 28, '英语': 5},
    '林深': {'语文': 44, '数学': 86, '英语': 73},
    '刘佳莹': {'语文': 99, '数学': 95, '英语': 95},
    '张莹': {'语文': 98, '数学': 65, '英语': 100},
    '武成龙': {'语文': 77, '数学': 97, '英语': 65},
}


def avg(lst):
    return sum(lst) / len(lst)


lst = []
yuwen = {}
shuxue = {}
yingyu = {}

for name, score_dic in data.items():
    score_list = score_dic.values()
    yuwen[name] = (score_dic.get('语文', 0))
    shuxue[name] = (score_dic.get('数学', 0))
    yingyu[name] = (score_dic.get('英语', 0))
    score_dic.get('英语', 0)
    if avg(score_list) < 60:
        lst.append(name)

print('各科综合平均分不足60的同学为：', ' '.join(lst))
print('语文最高分%d, 数学最高分%d, 英语最高分%d' % (max(yuwen.values()), max(shuxue.values()), max(yingyu.values())))
print('语文平均分%d, 数学平均分%d, 英语平均分%d' % (avg(yuwen.values()), avg(shuxue.values()), avg(yingyu.values())))
print(
    '语文学霸:%s, 数学学霸:%s, 英语学霸:%s' % (max(yuwen, key=yuwen.get), max(shuxue, key=shuxue.get), max(yingyu, key=yingyu.get)))


# 生成get请求地址的方法
def url_format(domain, url=None, data=None):
    result = 'http://' + domain
    if url:
        result = result + '/' + url
    if data:
        list = []
        for k, v in data.items():
            list.append(str(k) + '=' + str(v))
        result = result + '?' + '&'.join(list)
    return result


print(url_format('127.0.0.1', 'huice/api', {'name': 'tiantian', 'password': '123'}))


# 递归实现阶乘
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


print(fact(5))


# 递归实现回声
def fact_voice(context):
    print(context)
    context = context[1:]

    if len(context) != 0:
        return fact_voice(context)


fact_voice(u'同志们你们好吗')
