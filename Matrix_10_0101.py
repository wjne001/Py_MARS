#将含有多个符号的表达式的系数分奇偶数进行调整，并查找加解密矩阵中特定元素（（“1”和“F(f，u)+1”））
from sympy import symbols, Poly, Matrix, expand, factor


# 创建符号变量
#f, u0, u1, u2, u3 = symbols('f u0 u1 u2 u3')
f, f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, f_9, f_10, f_11, f_12, fn, u0, u1, u2, u3 = symbols('f f_1 f_2 f_3 f_4 f_5 f_6 f_7 f_8 f_9 f_10 f_11 f_12 fn u0 u1 u2 u3')
#函数modify_coefficients()用于将矩阵相乘相加结果进行异或转换
def modify_coefficients(expression):
    #as_coefficients_dict()输出为字典类型，(<class 'int'>, {x**2: 3, y**2: 4, x*y: 2})
    terms = expression.as_coefficients_dict() 
    #用于存储新的表达式
    new_terms = 0
    #遍历terms字典中的系数，系数为奇数将其赋值为1，偶数赋值为0
    for term,coeff in terms.items():
        new_coeff = 1 if coeff % 2 else 0  # 判断系数是否为奇数
        new_terms += term * new_coeff
    return new_terms

def campare_coefficients(expression):
    #expr_1 = x**5 + 4*x**2 + 3*x*y + 5*x  + 1
    #as_coefficients_dict()输出为字典类型，(<class 'int'>, {1: 1, x**5: 1, x**2: 4, x: 5, x*y: 3})
    term = expression.as_coefficients_dict()
    #使用keys()，获取字典的键值，dict_keys([1, x**5, x**2, x, x*y])
    element = term.keys()
    #使用list(),将dict_keys转换为列表类型
    l_1 = list(element)

    #0进行单独处理否则报错，0元素输出对应字典类型为<class 'int'>, {1: 0})，再取键值为1，与元素1相同了
    if expression == 0:
    #if len(l_1) == 1 and l_1[0] == 0:   #0
        value = 0
    else:
        if len(l_1) == 1 and l_1[0] == 1:    #1
            value = 1
        elif len(l_1) == 2 and (l_1[0] == 1 or  l_1[1] == 1):  #fn+1
            value = fn+1
        elif len(l_1) == 1 and (l_1[0] != 1 and l_1[0] != 0):  #fn
            value = fn
        else:
            value = '/'

    return(value)



#类MARS一般结构混淆矩阵
H = Matrix([
    [1,f,f,f],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]])
H_ni = Matrix([
    [1,f,f,f],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]])
'''
#类MARS一般结构扩散矩阵
P = Matrix([
    [0,0,0,1],
    [1,0,0,u0],
    [u1,1,0,u2],
    [u3,0,1,0]])
'''
#类MARS一般结构扩散矩阵
P = Matrix([
    [0,0,0,1],
    [1,0,0,0],
    [1,1,0,0],
    [1,0,1,0]])
P_ni = Matrix([
    [0,1,0,0],
    [0,1,1,0],
    [0,0,0,1],
    [1,0,0,0]])
#print(P.inv()*H_ni)

#类MARS一般结构一轮加密矩阵M_1 = HP,解密矩阵M_ni_1=P_ni*H_in
#由M_1 = H*P计算可得
M_1 = Matrix([
    [f_1, f_1, f_1, 1], 
    [1, 0, 0, 0], 
    [1, 1, 0, 0], 
    [1, 0, 1, 0]])
M_2 = Matrix([
    [f_2, f_2, f_2, 1], 
    [1, 0, 0, 0], 
    [1, 1, 0, 0], 
    [1, 0, 1, 0]])
M_3 = Matrix([
    [f_3, f_3, f_3, 1], 
    [1, 0, 0, 0], 
    [1, 1, 0, 0], 
    [1, 0, 1, 0]])
M_4 = Matrix([
    [f_4, f_4, f_4, 1], 
    [1, 0, 0, 0], 
    [1, 1, 0, 0], 
    [1, 0, 1, 0]])
M_5 = Matrix([
    [f_5, f_5, f_5, 1], 
    [1, 0, 0, 0], 
    [1, 1, 0, 0], 
    [1, 0, 1, 0]])
M_6 = Matrix([
    [f_6, f_6, f_6, 1], 
    [1, 0, 0, 0], 
    [1, 1, 0, 0], 
    [1, 0, 1, 0]])
M_7 = Matrix([
    [f_7, f_7, f_7, 1], 
    [1, 0, 0, 0], 
    [1, 1, 0, 0], 
    [1, 0, 1, 0]])
M_8 = Matrix([
    [f_8, f_8, f_8, 1], 
    [1, 0, 0, 0], 
    [1, 1, 0, 0], 
    [1, 0, 1, 0]])
M_9 = Matrix([
    [f_9, f_9, f_9, 1], 
    [1, 0, 0, 0], 
    [1, 1, 0, 0], 
    [1, 0, 1, 0]])
M_10 = Matrix([
    [f_10, f_10, f_10, 1], 
    [1, 0, 0, 0], 
    [1, 1, 0, 0], 
    [1, 0, 1, 0]])
M_11 = Matrix([
    [f_11, f_11, f_11, 1], 
    [1, 0, 0, 0], 
    [1, 1, 0, 0], 
    [1, 0, 1, 0]])
M_12 = Matrix([
    [f_12, f_12, f_12, 1], 
    [1, 0, 0, 0], 
    [1, 1, 0, 0], 
    [1, 0, 1, 0]])
#由M_ni_1 = P.inv()*H.inv()计算可得
M_ni_1 = Matrix([
    [0, 1, 0, 0], 
    [0, 1, 1, 0], 
    [0, 1, 0, 1], 
    [1, f_1, f_1, f_1]])
M_ni_2 = Matrix([
    [0, 1, 0, 0], 
    [0, 1, 1, 0], 
    [0, 1, 0, 1], 
    [1, f_2, f_2, f_2]])
M_ni_3 = Matrix([
    [0, 1, 0, 0], 
    [0, 1, 1, 0], 
    [0, 1, 0, 1], 
    [1, f_3, f_3, f_3]])
M_ni_4 = Matrix([
    [0, 1, 0, 0], 
    [0, 1, 1, 0], 
    [0, 1, 0, 1], 
    [1, f_4, f_4, f_4]])
M_ni_5 = Matrix([
    [0, 1, 0, 0], 
    [0, 1, 1, 0], 
    [0, 1, 0, 1], 
    [1, f_5, f_5, f_5]])
M_ni_6 = Matrix([
    [0, 1, 0, 0], 
    [0, 1, 1, 0], 
    [0, 1, 0, 1], 
    [1, f_6, f_6, f_6]])
M_ni_7 = Matrix([
    [0, 1, 0, 0], 
    [0, 1, 1, 0], 
    [0, 1, 0, 1], 
    [1, f_7, f_7, f_7]])
M_ni_8 = Matrix([
    [0, 1, 0, 0], 
    [0, 1, 1, 0], 
    [0, 1, 0, 1], 
    [1, f_8, f_8, f_8]])
M_ni_9 = Matrix([
    [0, 1, 0, 0], 
    [0, 1, 1, 0], 
    [0, 1, 0, 1], 
    [1, f_9, f_9, f_9]])
M_ni_10 = Matrix([
    [0, 1, 0, 0], 
    [0, 1, 1, 0], 
    [0, 1, 0, 1], 
    [1, f_10, f_10, f_10]])
M_ni_11 = Matrix([
    [0, 1, 0, 0], 
    [0, 1, 1, 0], 
    [0, 1, 0, 1], 
    [1, f_11, f_11, f_11]])
M_ni_12 = Matrix([
    [0, 1, 0, 0], 
    [0, 1, 1, 0], 
    [0, 1, 0, 1], 
    [1, f_12, f_12, f_12]])
#类MARS特殊结构n轮（多轮）加密矩阵为M_2，解密矩阵为M_ni_2
#用expand()函数确保结果为展开式
M_n = expand(M_1*M_2*M_3*M_4*M_5*M_6)
#M_n = expand(M_ni_1*M_ni_2*M_ni_3*M_ni_4*M_ni_5*M_ni_6*M_ni_7*M_ni_8*M_ni_9*M_ni_10)


#创建一个新的矩阵，用于存储模2处理后的结果
new_M_n = Matrix.zeros(4,4)
for i in range(0,4):
    for j in range(0,4):
        new_M_n[i,j] = modify_coefficients(M_n[i,j])
print('n轮加密特征矩阵为：')
print(new_M_n)

#创建空列表，用于存储差分向量组合值，将4X4阶矩阵的每一行看做一个差分向量
#共有4X15=60种组合，0-0,1-1,2-2,3-3,4-01,5-02,6-03,7-12,8-13,9-23,10-012,11-013,12-023,13-123，14-0123
list_1 = []     #存储矩阵第1行组合
list_2 = []     #存储矩阵第2行组合
list_3 = []     #存储矩阵第3行组合
list_4 = []     #存储矩阵第4行组合

#矩阵第一行
list_1.append(modify_coefficients(new_M_n[0,0]))
list_1.append(modify_coefficients(new_M_n[0,1]))
list_1.append(modify_coefficients(new_M_n[0,2]))
list_1.append(modify_coefficients(new_M_n[0,3]))
list_1.append(modify_coefficients(new_M_n[0,0] + new_M_n[0,1]))
list_1.append(modify_coefficients(new_M_n[0,0] + new_M_n[0,2]))
list_1.append(modify_coefficients(new_M_n[0,0] + new_M_n[0,3]))
list_1.append(modify_coefficients(new_M_n[0,1] + new_M_n[0,2]))
list_1.append(modify_coefficients(new_M_n[0,1] + new_M_n[0,3]))
list_1.append(modify_coefficients(new_M_n[0,2] + new_M_n[0,3]))
list_1.append(modify_coefficients(new_M_n[0,0] + new_M_n[0,1] + new_M_n[0,2]))
list_1.append(modify_coefficients(new_M_n[0,0] + new_M_n[0,1] + new_M_n[0,3]))
list_1.append(modify_coefficients(new_M_n[0,0] + new_M_n[0,2] + new_M_n[0,3]))
list_1.append(modify_coefficients(new_M_n[0,1] + new_M_n[0,2] + new_M_n[0,3]))
list_1.append(modify_coefficients(new_M_n[0,0] + new_M_n[0,1] + new_M_n[0,2] + new_M_n[0,3]))
#矩阵第二行
list_2.append(modify_coefficients(new_M_n[1,0]))
list_2.append(modify_coefficients(new_M_n[1,1]))
list_2.append(modify_coefficients(new_M_n[1,2]))
list_2.append(modify_coefficients(new_M_n[1,3]))
list_2.append(modify_coefficients(new_M_n[1,0] + new_M_n[1,1]))
list_2.append(modify_coefficients(new_M_n[1,0] + new_M_n[1,2]))
list_2.append(modify_coefficients(new_M_n[1,0] + new_M_n[1,3]))
list_2.append(modify_coefficients(new_M_n[1,1] + new_M_n[1,2]))
list_2.append(modify_coefficients(new_M_n[1,1] + new_M_n[1,3]))
list_2.append(modify_coefficients(new_M_n[1,2] + new_M_n[1,3]))
list_2.append(modify_coefficients(new_M_n[1,0] + new_M_n[1,1] + new_M_n[1,2]))
list_2.append(modify_coefficients(new_M_n[1,0] + new_M_n[1,1] + new_M_n[1,3]))
list_2.append(modify_coefficients(new_M_n[1,0] + new_M_n[1,2] + new_M_n[1,3]))
list_2.append(modify_coefficients(new_M_n[1,1] + new_M_n[1,2] + new_M_n[1,3]))
list_2.append(modify_coefficients(new_M_n[1,0] + new_M_n[1,1] + new_M_n[1,2] + new_M_n[1,3]))
#矩阵第三行
list_3.append(modify_coefficients(new_M_n[2,0]))
list_3.append(modify_coefficients(new_M_n[2,1]))
list_3.append(modify_coefficients(new_M_n[2,2]))
list_3.append(modify_coefficients(new_M_n[2,3]))
list_3.append(modify_coefficients(new_M_n[2,0] + new_M_n[2,1]))
list_3.append(modify_coefficients(new_M_n[2,0] + new_M_n[2,2]))
list_3.append(modify_coefficients(new_M_n[2,0] + new_M_n[2,3]))
list_3.append(modify_coefficients(new_M_n[2,1] + new_M_n[2,2]))
list_3.append(modify_coefficients(new_M_n[2,1] + new_M_n[2,3]))
list_3.append(modify_coefficients(new_M_n[2,2] + new_M_n[2,3]))
list_3.append(modify_coefficients(new_M_n[2,0] + new_M_n[2,1] + new_M_n[2,2]))
list_3.append(modify_coefficients(new_M_n[2,0] + new_M_n[2,1] + new_M_n[2,3]))
list_3.append(modify_coefficients(new_M_n[2,0] + new_M_n[2,2] + new_M_n[2,3]))
list_3.append(modify_coefficients(new_M_n[2,1] + new_M_n[2,2] + new_M_n[2,3]))
list_3.append(modify_coefficients(new_M_n[2,0] + new_M_n[2,1] + new_M_n[2,2] + new_M_n[2,3]))
#矩阵第四行
list_4.append(modify_coefficients(new_M_n[3,0]))
list_4.append(modify_coefficients(new_M_n[3,1]))
list_4.append(modify_coefficients(new_M_n[3,2]))
list_4.append(modify_coefficients(new_M_n[3,3]))
list_4.append(modify_coefficients(new_M_n[3,0] + new_M_n[3,1]))
list_4.append(modify_coefficients(new_M_n[3,0] + new_M_n[3,2]))
list_4.append(modify_coefficients(new_M_n[3,0] + new_M_n[3,3]))
list_4.append(modify_coefficients(new_M_n[3,1] + new_M_n[3,2]))
list_4.append(modify_coefficients(new_M_n[3,1] + new_M_n[3,3]))
list_4.append(modify_coefficients(new_M_n[3,2] + new_M_n[3,3]))
list_4.append(modify_coefficients(new_M_n[3,0] + new_M_n[3,1] + new_M_n[3,2]))
list_4.append(modify_coefficients(new_M_n[3,0] + new_M_n[3,1] + new_M_n[3,3]))
list_4.append(modify_coefficients(new_M_n[3,0] + new_M_n[3,2] + new_M_n[3,3]))
list_4.append(modify_coefficients(new_M_n[3,1] + new_M_n[3,2] + new_M_n[3,3]))
list_4.append(modify_coefficients(new_M_n[3,0] + new_M_n[3,1] + new_M_n[3,2] + new_M_n[3,3]))


#第一行
#print('第1行组合：')
#print(list_1)
#创建空列表，用于存储矩阵每一行差分向量组合的转换值
list_transform_1 = []
for i in range(0,15):
    list_transform_1.append(campare_coefficients(list_1[i]))
print('第1行组合对应判断值：')
print(list_transform_1)

#第二行
#print('第2行组合：')
#print(list_2)
#创建空列表，用于存储矩阵每一行差分向量组合的转换值
list_transform_2 = []
for i in range(0,15):
    list_transform_2.append(campare_coefficients(list_2[i]))
print('第2行组合对应判断值：')
print(list_transform_2) 

#第三行
#print('第3行组合：')
#print(list_3)
#创建空列表，用于存储矩阵每一行差分向量组合的转换值
list_transform_3 = []
for i in range(0,15):
    list_transform_3.append(campare_coefficients(list_3[i]))
print('第3行组合对应判断值：')
print(list_transform_3)

#第四行
#print('第4行组合：')
#print(list_4)
#创建空列表，用于存储矩阵每一行差分向量组合的转换值
list_transform_4 = []
for i in range(0,15):
    list_transform_4.append(campare_coefficients(list_4[i]))
print('第4行组合对应判断值：')
print(list_transform_4)

