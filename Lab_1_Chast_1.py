"МОДЕЛИРОВАНИЕ НЕПРЕРЫВНЫХ И ДИСКРЕТНЫХ СЛУЧАЙНЫХ ВЕЛИЧИН: непрерывные"

import numpy as np
import random
import pandas as pa
import scipy as sc
import math
import matplotlib.pyplot as plt
import sympy as sp


plotrasp=0.25 #плотность
#[0;4] интервал распределения 
#размеры выборки N = 50, N = 200, N = 1000
# ф-я распределения F(x) = 0.25x
# x = 4z
#случайная величина, подчиняющаяся закону распределения:

z1 = np.array([random.random() for i in range(50)])
z2 = np.array([random.random() for i in range(200)])
z3 = np.array([random.random() for i in range(1000)])
x1 = 4 * z1 
x2 = 4 * z2 
x3 = 4 * z3 

Srednee1 = np.mean(x1) # оценка среднее
# как считать вручную
#M2 = 1/200 * (sum(4 * z2))
#M3 = 1/1000 * (sum(4 * z3))
Srednee2 = np.mean(x2)
Srednee3 = np.mean(x3)
#print(Srednee1)
Dispers1 = np.var(x1) # дисперсия
Dispers2 = np.var(x2)
Dispers3 = np.var(x3)
#print(Dispers1)
SKO1 = np.std(x1) # среднеквадратич отклон
SKO2 = np.std(x2)
SKO3 = np.std(x3)
#print(SKO1)





# тут начинается отсебятина


# ИНТЕРВАЛЬНАЯ ОЦЕНКА СРЕДНЕГО
#print("ИНТЕРВАЛЬНАЯ ОЦЕНКА СРЕДНЕГО")
#print("a = 0.1")
n50_01 = sc.stats.t.ppf(1- .1/2, 49) #коэффициент стьюдента при уровне значимости 0.1 и уровне свободы = 49
NijneeSred1 = Srednee1 - (n50_01 * (SKO1/(50**(1/2)))) #верхняя граница для интервальной оценки среднего
VerhSred1 = Srednee1 + (n50_01 * (SKO1/(50**(1/2)))) #нижняя граница для интервальной оценки среднего

n200_01 = sc.stats.t.ppf(1- .1/2, 199) #коэффициент стьюдента при уровне значимости 0.1 и уровне свободы = 199
NijneeSred2 = Srednee2 - (n200_01 * (SKO2/(200**(1/2))))
VerhSred2 = Srednee2 + (n200_01 * (SKO2/(200**(1/2))))

n1000_01 = sc.stats.t.ppf(1- .1/2, 999)
NijneeSred3 = Srednee3 - (n1000_01 * (SKO3/(1000**(1/2))))
VerhSred3 = Srednee3 + (n1000_01 * (SKO3/(1000**(1/2))))

#print("a = 0.05")
n50_005 = sc.stats.t.ppf(1- .05/2, 49) #коэффициент стьюдента при уровне значимости 0.1 и уровне свободы = 49
NijneeSred1_2 = Srednee1 - (n50_005 * (SKO1/(50**(1/2)))) #верхняя граница для интервальной оценки среднего
VerhSred1_2 = Srednee1 + (n50_005 * (SKO1/(50**(1/2)))) #нижняя граница для интервальной оценки среднего

n200_005 = sc.stats.t.ppf(1- .05/2, 199) #коэффициент стьюдента при уровне значимости 0.1 и уровне свободы = 199
NijneeSred2_2 = Srednee2 - (n200_005 * (SKO2/(200**(1/2))))
VerhSred2_2 = Srednee2 + (n200_005 * (SKO2/(200**(1/2))))

n1000_005 = sc.stats.t.ppf(1- .05/2, 999)
NijneeSred3_2 = Srednee3 - (n1000_005 * (SKO3/(1000**(1/2))))
VerhSred3_2 = Srednee3 + (n1000_005 * (SKO3/(1000**(1/2))))

#print("a = 0.01")
n50_001 = sc.stats.t.ppf(1- .01/2, 49) #коэффициент стьюдента при уровне значимости 0.1 и уровне свободы = 49
NijneeSred1_3 = Srednee1 - (n50_001 * (SKO1/(50**(1/2)))) #верхняя граница для интервальной оценки среднего
VerhSred1_3 = Srednee1 + (n50_001 * (SKO1/(50**(1/2)))) #нижняя граница для интервальной оценки среднего

n200_001 = sc.stats.t.ppf(1- .01/2, 199) #коэффициент стьюдента при уровне значимости 0.1 и уровне свободы = 199
NijneeSred2_3 = Srednee2 - (n200_001 * (SKO2/(200**(1/2))))
VerhSred2_3 = Srednee2 + (n200_001 * (SKO2/(200**(1/2))))

n1000_001 = sc.stats.t.ppf(1- .01/2, 999)
NijneeSred3_3 = Srednee3 - (n1000_001 * (SKO3/(1000**(1/2))))
VerhSred3_3 = Srednee3 + (n1000_001 * (SKO3/(1000**(1/2))))






#ИНТЕРВАЛЬНАЯ ОЦЕНКА ДЛЯ ДИСПЕРСИИ
#print("ИНТЕРВАЛЬНАЯ ОЦЕНКА ДЛЯ ДИСПЕРСИИ")
#print("a = 0.1")
NijneeDisp1 = SKO1**2 * 49 / (sc.stats.chi2.ppf(1-.1/2, 49))
VerhDisp1 = SKO1**2 * 49 / (sc.stats.chi2.ppf(.1/2, 49))

NijneeDisp2 = SKO2**2 * 199 / (sc.stats.chi2.ppf(1-.1/2, 199))
VerhDisp2 = SKO2**2 * 199 / (sc.stats.chi2.ppf(.1/2, 199))

NijneeDisp3 = SKO3**2 * 999 / (sc.stats.chi2.ppf(1-.1/2, 999))
VerhDisp3 = SKO3**2 * 999 / (sc.stats.chi2.ppf(.1/2, 999))

#print("a = 0.05")
NijneeDisp1_2 = SKO1**2 * 49 / (sc.stats.chi2.ppf(1-.05/2, 49))
VerhDisp1_2 = SKO1**2 * 49 / (sc.stats.chi2.ppf(.05/2, 49))

NijneeDisp2_2 = SKO2**2 * 199 / (sc.stats.chi2.ppf(1-.05/2, 199))
VerhDisp2_2 = SKO2**2 * 199 / (sc.stats.chi2.ppf(.05/2, 199))

NijneeDisp3_2 = SKO3**2 * 999 / (sc.stats.chi2.ppf(1-.05/2, 999))
VerhDisp3_2 = SKO3**2 * 999 / (sc.stats.chi2.ppf(.05/2, 999))

#print("a = 0.01")
NijneeDisp1_3 = SKO1**2 * 49 / (sc.stats.chi2.ppf(1-.01/2, 49))
VerhDisp1_3 = SKO1**2 * 49 / (sc.stats.chi2.ppf(.01/2, 49))

NijneeDisp2_3 = SKO2**2 * 199 / (sc.stats.chi2.ppf(1-.01/2, 199))
VerhDisp2_3 = SKO2**2 * 199 / (sc.stats.chi2.ppf(.01/2, 199))

NijneeDisp3_3 = SKO3**2 * 999 / (sc.stats.chi2.ppf(1-.01/2, 999))
VerhDisp3_3 = SKO3**2 * 999 / (sc.stats.chi2.ppf(.01/2, 999))




# для a = 0.1
data1 = {'Размер выборки':[50, 200, 1000], 'Нижняя граница оценки среднего': [NijneeSred1, NijneeSred2, NijneeSred3], \
        'Верхняя граница оценки среднего': [VerhSred1, VerhSred2, VerhSred3], 'Нижняя граница оценки дисперсии':[NijneeDisp1, NijneeDisp2, NijneeDisp3], \
            'Верхняя граница оценки дисперсии': [VerhDisp1, VerhDisp2, VerhDisp3]}
df = pa.DataFrame(data1, index = ['№1', '№2', '№3'])

print('Для N = 50 alpha = 0.1 точечная оценка среднего =', Srednee1, 'нижняя граница =', NijneeSred1, 'верхняя граница =', VerhSred1)
print('Для N = 200 alpha = 0.1 точечная оценка среднего =', Srednee2, 'нижняя граница =', NijneeSred2, 'верхняя граница =', VerhSred2)
print('Для N = 1000 alpha = 0.1 точечная оценка среднего =', Srednee3, 'нижняя граница =', NijneeSred3, 'верхняя граница =', VerhSred3)

print('Для N = 50 alpha = 0.1 точечная оценка дисперсии =', Dispers1, 'нижняя граница =', NijneeDisp1, 'верхняя граница =', VerhDisp1)
print('Для N = 200 alpha = 0.1 точечная оценка дисперсии =', Dispers2, 'нижняя граница =', NijneeDisp2, 'верхняя граница =', VerhDisp2)
print('Для N = 1000 alpha = 0.1 точечная оценка дисперсии =', Dispers3, 'нижняя граница =', NijneeDisp3, 'верхняя граница =', VerhDisp3)



# для a = 0.05
data2 = {'Размер выборки':[50, 200, 1000], 'Нижняя граница оценки среднего': [NijneeSred1_2, NijneeSred2_2, NijneeSred3_2], \
        'Верхняя граница оценки среднего': [VerhSred1_2, VerhSred2_2, VerhSred3_2], \
            'Нижняя граница оценки дисперсии':[NijneeDisp1_2, NijneeDisp2_2, NijneeDisp3_2], \
                'Верхняя граница оценки дисперсии': [VerhDisp1_2, VerhDisp2_2, VerhDisp3_2]}

print('Для N = 50 alpha = 0.05 точечная оценка среднего =', Srednee1, 'нижняя граница =', NijneeSred1_2, 'верхняя граница =', VerhSred1_2)
print('Для N = 200 alpha = 0.05 точечная оценка среднего =', Srednee2, 'нижняя граница =', NijneeSred2_2, 'верхняя граница =', VerhSred2_2)
print('Для N = 1000 alpha = 0.05 точечная оценка среднего =', Srednee3, 'нижняя граница =', NijneeSred3_2, 'верхняя граница =', VerhSred3_2)

print('Для N = 50 alpha = 0.05 точечная оценка дисперсии =', Dispers1, 'нижняя граница =', NijneeDisp1_2, 'верхняя граница =', VerhDisp1_2)
print('Для N = 200 alpha = 0.05 точечная оценка дисперсии =', Dispers2, 'нижняя граница =', NijneeDisp2_2, 'верхняя граница =', VerhDisp2_2)
print('Для N = 1000 alpha = 0.05 точечная оценка дисперсии =', Dispers3, 'нижняя граница =', NijneeDisp3_2, 'верхняя граница =', VerhDisp3_2)


# для a = 0.01
data3 = {'Размер выборки':[50, 200, 1000], 'Нижняя граница оценки среднего': [NijneeSred1_3, NijneeSred2_3, NijneeSred3_3], \
        'Верхняя граница оценки среднего': [VerhSred1_3, VerhSred2_3, VerhSred3_3], \
            'Нижняя граница оценки дисперсии':[NijneeDisp1_3, NijneeDisp2_3, NijneeDisp3_3], \
                'Верхняя граница оценки дисперсии': [VerhDisp1_3, VerhDisp2_3, VerhDisp3_3]}

print('Для N = 50 alpha = 0.01 точечная оценка среднего =', Srednee1, 'нижняя граница =', NijneeSred1_3, 'верхняя граница =', VerhSred1_3)
print('Для N = 200 alpha = 0.01 точечная оценка среднего =', Srednee2, 'нижняя граница =', NijneeSred2_3, 'верхняя граница =', VerhSred2_3)
print('Для N = 1000 alpha = 0.01 точечная оценка среднего =', Srednee3, 'нижняя граница =', NijneeSred3_3, 'верхняя граница =', VerhSred3_3)

print('Для N = 50 alpha = 0.01 точечная оценка дисперсии =', Dispers1, 'нижняя граница =', NijneeDisp1_3, 'верхняя граница =', VerhDisp1_3)
print('Для N = 200 alpha = 0.01 точечная оценка дисперсии =', Dispers2, 'нижняя граница =', NijneeDisp2_3, 'верхняя граница =', VerhDisp2_3)
print('Для N = 1000 alpha = 0.01 точечная оценка дисперсии =', Dispers3, 'нижняя граница =', NijneeDisp3_3, 'верхняя граница =', VerhDisp3_3)

#print(df)
df1 = pa.DataFrame(data1, index = ['№1', '№2', '№3'])
df2 = pa.DataFrame(data2, index = ['№1', '№2', '№3'])
df3 = pa.DataFrame(data3, index = ['№1', '№2', '№3'])
with pa.ExcelWriter('Test.xlsx') as writer:  
    df1.to_excel(writer, sheet_name = 'Для alpa = 0.1')
    df2.to_excel(writer, sheet_name = 'Для alpa = 0.05')
    df3.to_excel(writer, sheet_name = 'Для alpha = 0.01')


# часть с офигенными графиками
# аж больно стало

k = 1 + 3.322 * math.log(50)
k = 14
#plt.hist(z..., bins = 14)
#plt.show()

x = sp.Symbol('x')
function_y = sp.sympify('0.25')
interval = np.arange(0, 4, 0.01)
y_values = [function_y.subs(x, value) for value in interval]

plt.plot(interval, y_values, 'r')
plt.hist(x1, bins = k, density = True)
plt.title('N = 50')
plt.show()
#print(x1)

k = 19
plt.plot(interval, y_values, 'r')
plt.hist(x2, bins = k, density = True)
plt.title('N = 200')
plt.show()

k = 24
plt.plot(interval, y_values, 'r')
plt.hist(x3, bins = k, density = True)
plt.title('N = 1000')
plt.show()




#Графики Распределение вероятности(красная) Плотность распределения вероятности(синий)
x_1 = np.arange(0,4,0.01)
y_1 = 0.25 + (x_1)*0
plt.plot(x_1,y_1,color = 'b')

x_1 = np.arange(4,6,0.01)
y_1 = x_1*0
plt.plot(x_1,y_1,color = 'b')

x_1 = np.arange(0,4,0.01)
y_1 = x_1/4
plt.plot(x_1,y_1,color='r')

x_1 = np.arange(4,6,0.01)
y_1 = (x_1*0) + 1

plt.plot(x_1,y_1,color='r')

plt.title('Распределение вероятности(красная) \n Плотность распределения вероятности(синий)')

plt.show()









