"""给你一个长度为n的数组，其中只有一个数字出现大于n / 2次，问如何快速找到这个数字（20分）"""
def find_nun(list):
    list.sort()
    i=len(list)//2
    num=list[i]
    return num
list01=[1,3,3,3,0,3,5,6,7]
print(find_nun(list01))

"""
输入一个正数n，输出所有和为n 连续正数序列。（20分）
例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以输出3 个连续序列1-5、4-6 和7-8。
"""
list02=[]
def func(n):
    for x in range(1,n//2+1):
        for y in range(x+1,n):
            if (x+y)*((y-x+1)/2)==n:
                list02.append((x,y))
                break
func(34)
print(list02)

"""
假设给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。
最小的 24 小时制时间是 00:00，而最大的是 23:59。
从 00:00 （午夜）开始算起，过得越久，时间越大。以长度为 5 的字符串返回。(30分)
示例  输入：[1,2,3,4] 输出："23:41"
"""
list03=[]
l01=[0,1,2]
def find_list(l):
    for x in l[-1::-1]:
        if x>2:
            continue
        l.remove(x)
        for y in l01[-1::-1]:
            if x ==0 or x==1 or (x==2 and l[y]<4):
                l01.remove(y)
                str01 = "%d%d:%d%d" % (x,l[y] , l[l01[0]], l[l01[1]])
                str02 = "%d%d:%d%d" % (x,l[y],l[l01[1]],l[l01[0]])
                if l[l01[0]]<6 and str01 not in list03:
                        list03.append(str01)

                if l[l01[1]]<6 and str02 not in list03:
                        list03.append(str02)
                l01.append(y)
        l.append(x)
l04=[5,0,3,4]
find_list(l04)
print(list03)
def find_time(l):
    max_time=l[0]
    for i in range( len(l)-1):
        if int(l[i+1][0:2]) > int(max_time[0:2]):
            max_time=l[i+1]
        elif int(l[i+1][0:2])==int(max_time[0:2]):
            if int(l[i+1][3:5])>int(max_time[3:5]):
                max_time=l[i+1]
    return max_time
print(find_time(list03))