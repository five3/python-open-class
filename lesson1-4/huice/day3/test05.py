# 1. 快速排序就是选定一个标志位，我们把它叫做flag，
# 把小于flag的放在它的左边，把大于flag的放在它的右边，这样就以flag的分界，
# 把原来的list分为了两个子list ： list1 和 list2。
# 2. 按照上述方法，在list1 和 list2中再分别选flag，将list1 和 list2 分别拆成两个list，依次类推
# 3. 直到n = 1，即每个子list都只有一个元素  整个过程 : n/2x = 1  x = log2n

def quick_sort(aList = []):
    if len(aList)<=1:
        return aList
    else:
        flag = aList[0] #任意选一个值作为flag
        smallerList = [] #存放比flag小的值
        biggerList = [] #存放比flag大的值
        flags = []
        for i in aList:
            if i<flag:
                smallerList.append(i)
            elif i>flag:
                biggerList.append(i)
            else:
                flags.append(flag)

        # 递归调用
        smallerList = quick_sort(smallerList)
        biggerList = quick_sort(biggerList)

        return smallerList+flags+biggerList

list2sort = [30,20,10,90,80,50]
print(quick_sort(list2sort))