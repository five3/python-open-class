# 题1：给定一个IP文件（每行一个ip地址）。打印出重复次数最多的IP和对应的次数def find_max_count_ip(fn):    with open(fn, 'r', encoding='utf8') as f:        for ip in f:            print(ip, end='')            # TODO:if "__main__" == __name__:    find_max_count_ip('ip')    # 找到出现次数最多前N个IP"""# 题2：给定字符串，对单词进行反转e.g. hello python => olleh nohtyp"""