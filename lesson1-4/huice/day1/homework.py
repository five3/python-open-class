s = "asdasj678596knxcn213123982930knsdns,mnfsdh234898ncmdnsdkj"
# 取出给定字符串中的数字，并打印出是偶数的字符，当打印次数大于10时退出
# e.g. 上文会打印出：6862282024


def find_max_count_ip(fn):
    with open(fn, 'r', encoding='utf8') as f:
        for ip in f:
            print(ip, end='')
            # TODO:


if "__main__" == __name__:
    find_max_count_ip('ip')
    # 找到出现次数最多前N个IP
