# print("hello world")    #字符串
# print(23333)            #整数
# print(2.3333)
# print(True)
# print(False)
# print(())
# print([])
# print({})
# """sdjf;jdsafjsdaf"""
# print(23333, "哈哈哈哈")
# # print("哈哈" + "嘻嘻")  #字符串的拼接，只能同样的数据类型进行操作
# # print("哈哈哈" * 2)

# """
# 练习：通过代码获取两段内容，并且计算他们的长度的和
# """

# a = input("请输入第一段内容：")
# b = input("请输入第二段内容：")
# print("两段字符串的长度是：", len(a) + len(b))




#元组o，下标，从0开始编号
# a = (1, 2, 3, 4, "哈哈", "嘻嘻", True, False)  #空的元组
#print(a[5])

#print(a.index("嘻嘻"))
#index 就近原则检索
#count 统计某个值的数量


#二维元祖
# b = (a, "哈哈", "嘻嘻")
# print(b[0][3]) 

#切片
# print(a[0:2])#左闭右开

# print(a[2:5])
# print(a[2:])

#元组一但写好后不可以修改，而数组时可以修改的
# a = [1, 2, 3, 4, "哈哈", "嘻嘻", True, False]
# a.append("append1")
# a.append("append2")  #往数组中追加数据（放到最后面）
# a.insert(4, "insert")#往数组中指定的位置插入数据
# print(a)
 #剪切，把数据从数组中拿出来
# b = a.pop(0)
# c = a.pop(0)
# print(b+c)
# print(b)
# print(c)

#a.clear()  清空数据
#a.extend() #可以将数组添加到数组中
# """
# 字典的特点
# 1、字典种的值没有顺序。
# 2、字典的结构必须是  键值对的结构。 key:value
# 3、字典的取值是通过key去取这个value
# 4、字符都要打引号
# """

# a = {
#     "name":"张三",
#     0:"哈哈",
#     "age":25
# }

#数组和字典的删除
# del a["name"]
# print(a)

# del a[0]

"""
练习：
获取用户输入的个人信息，并且存储到字典中。
个人信息包括，name、age、sex.
"""
name = input("输入用户的姓名：")
age = input("输入用户的年龄：")
sex = input("输入用户的性别：")
a = {"name":name, "age":age, "sex":sex}
print(a)