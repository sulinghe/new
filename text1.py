"""
1. 小明家必须要过一座桥。小明过桥最快要１秒，小明的弟弟最快要３秒，小明的爸爸最快要６秒，小明的妈妈最快要８秒，小明的爷爷最快要１２秒。每次此桥最多可过两人，而过桥的速度依过桥最慢者而定。过桥时候是黑夜，所以必须有手电筒，小明家只有一个手电筒，而且手电筒的电池只剩30秒就将耗尽。小明一家该如何过桥，请写出详细过程。

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
编程题（20分）
1. 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
1 <= 数组长度 <= 10000

示例:
输入: [0,1,2,3,4,5,6,7,9]

"""
len1=0
list1=[]
while True:
    length=int(input("请输入数组长度："))
    if length >=1 and length<=10000:
        len1=length
        break
for i in range(len1-1):
    while True:
        num=int(input("请输入数组元素："))
        if num >=0 and num<=len1-1:
            list1.append(num)
            break
    i+=1

re=0
for i in range(len1-2):
    list1.sort()
    if (list1[i+1]-list1[i])==2:
        re=list1[i]+1
    else:
        re=list1[-1]+1
    i+=1
print(re)









