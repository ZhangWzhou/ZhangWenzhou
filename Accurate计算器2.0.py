"""
Created on Thur Aug 25 11:41 2022

@author: zhang
"""

# Accurate计算器2.0.1
# 使用须知：
# 1.本产品由Zhang Wenzhou于2022年8月研发
# 2.开放源代码 https://github.com/ZhangWzhou/ZhangWenzhou/blob/main/Accurate%E8%AE%A1%E7%AE%97%E5%99%A82.0.py
# 3.免费
# 4.只适用于日常计算，不适用于科学计算

print("欢迎使用Accurate计算器 2.0.1!")
print("本计算器提供算术运算：加法（+）、减法（-）、乘法（*）、除法（/）、取余除（%）、取整除（//）、乘方（**）七种运算；逻辑运算：and，or，not三种运算；比较运算：>=，==，<=,>，<五种运算；转换类型：int()整数类型、float()浮点类型、str()字符串类型。")
print("如果看到>>>提示符即可输入运算表达式，按回车运算。")
print("如需终止运算请输入exit()。")
print("---------------------------------------------------------------------------------------------------------------")

while True:
    a = input(">>>")
    if a == "exit()":
        break
    if a == "":
        print(" ")
    else:
        print(eval(a))
    pass
pass
