# 题目：第一天1，第二天涨1，第三天跌1，第四天张一，第五条张一，第六天跌一
# 原理：1+-++-+++-++++-转换为1++++++++++++++--------
# 其中，+为天数n，-为原跌天数的2倍i
# 根据规律，间隔天数j要+1，跌的具体某一天k要累加迭代次数和间隔天数

def cal(day):
    i=0
    j=2
    k=2
    while(k < day):
        i=i+2
        j=j+1
        k=j+k
    return day - i

line = input()
while(line != ''):
    print(cal(int(line)))
    line=input()
