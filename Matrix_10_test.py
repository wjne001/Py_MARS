#使用python语言，利用sympy库获取多项表达式(含多个符号)中每一项的幂次和
from sympy import symbols, Poly

# 定义符号变量
x,y,z = symbols('x y z')

# 定义多项式表达式并
#expr = 3*x*y +4*x**2 + 5*x + 1
expr_1 = x**5 + 4*x**2 + x*y*z**2 + 3*x*y + 5*x  + 1
expr_2 = 3*x*y
expr_3 = 0*x**0

#as_coefficients_dict()输出为字典类型，(<class 'int'>, {1: 1, x**2: 4, x: 5, x*y: 3})
terms_1 = expr_1.as_coefficients_dict() 
terms_2 = expr_2.as_coefficients_dict() 
terms_3 = expr_3.as_coefficients_dict() 
print(terms_3)
#使用keys()，获取字典的键值，dict_keys([1, x**5, x**2, x, x*y, x*y*z**2])
element_1 = terms_1.keys()
element_2 = terms_2.keys()
element_3 = terms_3.keys()
#print(element)
#print(type(element))

'''
#使用set(),将dict_keys转换为集合类型
set_1 = set(element_1)
set_2 = set(element_2)
set_3 = set(element_3)
'''
#使用list(),将dict_keys转换为列表类型
list_1 = list(element_1)
list_2 = list(element_2)
list_3 = list(element_3)
print(list_1)
print(list_2)
print(list_3)

#使用len()求元素的个数
print(len(list_1))
print(len(list_2))
print(len(list_3))

if len(list_2) == 2 and (list_2[0] == 1 or  list_2[1] == 1):
	print("是fn+1")
if len(list_2) == 1 and list_2[0] != 1:
	print("是fn")
else:
	print('否')
#1
#0
#fn
#fn+1




