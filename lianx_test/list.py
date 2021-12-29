#"""
list = [1, 2, '晴天', 'python' ,'京东' ,'京东' ,'京东']#列表
C = len(list)
print(C)
av = list[0:3:4]#切片
print(av)
print(list.index(1)) #查看元素的下标
print(list.count('京东'))#统计


list.append('熊')#末尾增加

print(list)#打印

list.insert(1, '888')#在索引1位置增加

print(list)#

list.pop(0)   #删除0索引字段

print(list)
list.insert(-4, 'smart')#新增-4索引下字段

print('新增smart',list)

a = list[1] = '京东'#赋值
print(a)



