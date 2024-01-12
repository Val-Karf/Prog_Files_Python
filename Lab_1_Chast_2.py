"МОДЕЛИРОВАНИЕ НЕПРЕРЫВНЫХ И ДИСКРЕТНЫХ СЛУЧАЙНЫХ ВЕЛИЧИН: дискретные"

import numpy as np
import random
import pandas as pa
import scipy as sc
import math
import matplotlib.pyplot as plt
import sympy as sp
'''
def Random_puki(n):
    lst_1 = np.array([random.random() for i in range(n)]) # cоздаем сл велеч
    #print(lst_1)
    n_arr = np.array(range(1, n+1, 1))
    X = np.array([])
    for n in n_arr:
        s = lst_1[n - 1]
        i = 0
        s = s - ((0.5**i/math.factorial(i))*math.exp(-0.5))
        while s > 0:
            i += 1
            s = s - ((0.5**i/math.factorial(i))*math.exp(-0.5))
        else:
            X = np.append(X, i)
            print(lst_1[n - 1],X[-1],i)
    return (X)
'''
#пробуем задать массив Х не как нумпайский, а как классический список целочисленных, чтобы потом применить ф-ю каунт
def Random_puki(n):
    lst_1 = np.array([random.random() for i in range(n)]) # cоздаем сл велеч
    #print(lst_1)
    n_arr = np.array(range(1, n+1, 1))
    X = []
    for n in n_arr:
        s = lst_1[n - 1]
        i = 0
        s = s - ((0.5**i/math.factorial(i))*math.exp(-0.5))
        while s > 0:
            i += 1
            s = s - ((0.5**i/math.factorial(i))*math.exp(-0.5))
        else:
            X.append(i)
            print(lst_1[n - 1],X[-1],i)
    return X

def Vichislenia(x):
    mean_val = np.mean(x)
    disp_val = np.var(x)
    std_val = np.std(x)
    return mean_val, disp_val, std_val


v1 = Random_puki(50)
v2 = Random_puki(200)
v3 = Random_puki(1000)


variant1 = Vichislenia(v1)
variant2 = Vichislenia(v2)
variant3 = Vichislenia(v3)

# прогаем 4 пункт задания, смотрим верхнюю, нижнюю границы

# ИНТЕРВАЛЬНАЯ ОЦЕНКА СРЕДНЕГО
# alpha = 0.1
n50_01 = sc.stats.t.ppf(1- .1/2, 49) #коэффициент стьюдента при уровне значимости 0.1 и уровне свободы = 49
NijneeSred1 = variant1[0] - (n50_01 * (variant1[2]/(50**(1/2)))) #верхняя граница для интервальной оценки среднего
VerhSred1 = variant1[0] + (n50_01 * (variant1[2]/(50**(1/2)))) #нижняя граница для интервальной оценки среднего

n200_01 = sc.stats.t.ppf(1- .1/2, 199) 
NijneeSred2 = variant2[0] - (n200_01 * (variant2[2]/(200**(1/2))))
VerhSred2 = variant2[0] + (n200_01 * (variant2[2]/(200**(1/2))))

n1000_01 = sc.stats.t.ppf(1- .1/2, 999)
NijneeSred3 = variant3[0] - (n1000_01 * (variant3[2]/(1000**(1/2))))
VerhSred3 = variant3[0] + (n1000_01 * (variant3[2]/(1000**(1/2))))

#print(NijneeSred1)
#print(VerhSred1)

# alpha = 0.05
n50_005 = sc.stats.t.ppf(1- .05/2, 49) #коэффициент стьюдента при уровне значимости 0.1 и уровне свободы = 49
NijneeSred1_2 = variant1[0] - (n50_005 * (variant1[2]/(50**(1/2)))) #верхняя граница для интервальной оценки среднего
VerhSred1_2 = variant1[0] + (n50_005 * (variant1[2]/(50**(1/2)))) #нижняя граница для интервальной оценки среднего

n200_005 = sc.stats.t.ppf(1- .05/2, 199) 
NijneeSred2_2 = variant2[0] - (n200_005 * (variant2[2]/(200**(1/2))))
VerhSred2_2 = variant2[0] + (n200_005 * (variant2[2]/(200**(1/2))))

n1000_005 = sc.stats.t.ppf(1- .05/2, 999)
NijneeSred3_2 = variant3[0] - (n1000_005 * (variant3[2]/(1000**(1/2))))
VerhSred3_2 = variant3[0] + (n1000_005 * (variant3[2]/(1000**(1/2))))



# alpha = 0.01
n50_001 = sc.stats.t.ppf(1- .01/2, 49) #коэффициент стьюдента при уровне значимости 0.1 и уровне свободы = 49
NijneeSred1_3 = variant1[0] - (n50_001 * (variant1[2]/(50**(1/2)))) #верхняя граница для интервальной оценки среднего
VerhSred1_3 = variant1[0] + (n50_001 * (variant1[2]/(50**(1/2)))) #нижняя граница для интервальной оценки среднего

n200_001 = sc.stats.t.ppf(1- .01/2, 199) 
NijneeSred2_3 = variant2[0] - (n200_001 * (variant2[2]/(200**(1/2))))
VerhSred2_3 = variant2[0] + (n200_001 * (variant2[2]/(200**(1/2))))

n1000_001 = sc.stats.t.ppf(1- .01/2, 999)
NijneeSred3_3 = variant3[0] - (n1000_001 * (variant3[2]/(1000**(1/2))))
VerhSred3_3 = variant3[0] + (n1000_001 * (variant3[2]/(1000**(1/2))))





#ИНТЕРВАЛЬНАЯ ОЦЕНКА ДЛЯ ДИСПЕРСИИ
# alpha = 0.1
NijneeDisp1 = variant1[2]**2 * 49 / (sc.stats.chi2.ppf(1-.1/2, 49))
VerhDisp1 = variant1[2]**2 * 49 / (sc.stats.chi2.ppf(.1/2, 49))

NijneeDisp2 = variant2[2]**2 * 199 / (sc.stats.chi2.ppf(1-.1/2, 199))
VerhDisp2 = variant2[2]**2 * 199 / (sc.stats.chi2.ppf(.1/2, 199))

NijneeDisp3 = variant3[2]**2 * 999 / (sc.stats.chi2.ppf(1-.1/2, 999))
VerhDisp3 = variant3[2]**2 * 999 / (sc.stats.chi2.ppf(.1/2, 999))



# alpha = 0.05
NijneeDisp1_2 = variant1[2]**2 * 49 / (sc.stats.chi2.ppf(1-.05/2, 49))
VerhDisp1_2 = variant1[2]**2 * 49 / (sc.stats.chi2.ppf(.05/2, 49))

NijneeDisp2_2 = variant2[2]**2 * 199 / (sc.stats.chi2.ppf(1-.05/2, 199))
VerhDisp2_2 = variant2[2]**2 * 199 / (sc.stats.chi2.ppf(.05/2, 199))

NijneeDisp3_2 = variant3[2]**2 * 999 / (sc.stats.chi2.ppf(1-.05/2, 999))
VerhDisp3_2 = variant3[2]**2 * 999 / (sc.stats.chi2.ppf(.05/2, 999))



# alpha = 0.01
NijneeDisp1_3 = variant1[2]**2 * 49 / (sc.stats.chi2.ppf(1-.01/2, 49))
VerhDisp1_3 = variant1[2]**2 * 49 / (sc.stats.chi2.ppf(.01/2, 49))

NijneeDisp2_3 = variant2[2]**2 * 199 / (sc.stats.chi2.ppf(1-.01/2, 199))
VerhDisp2_3 = variant2[2]**2 * 199 / (sc.stats.chi2.ppf(.01/2, 199))

NijneeDisp3_3 = variant3[2]**2 * 999 / (sc.stats.chi2.ppf(1-.01/2, 999))
VerhDisp3_3 = variant3[2]**2 * 999 / (sc.stats.chi2.ppf(.01/2, 999))

#print(NijneeDisp3_3)
#print(VerhDisp3_3)

# записываем таблицы
# альфа = 0.1
data1 = {'Размер выборки':[50, 200, 1000], 'Нижняя граница оценки среднего': [NijneeSred1, NijneeSred2, NijneeSred3], \
        'Верхняя граница оценки среднего': [VerhSred1, VerhSred2, VerhSred3], 'Нижняя граница оценки дисперсии':[NijneeDisp1, NijneeDisp2, NijneeDisp3], \
            'Верхняя граница оценки дисперсии': [VerhDisp1, VerhDisp2, VerhDisp3]}

# альфа = 0.05
data2 = {'Размер выборки':[50, 200, 1000], 'Нижняя граница оценки среднего': [NijneeSred1_2, NijneeSred2_2, NijneeSred3_2], \
        'Верхняя граница оценки среднего': [VerhSred1_2, VerhSred2_2, VerhSred3_2], \
            'Нижняя граница оценки дисперсии':[NijneeDisp1_2, NijneeDisp2_2, NijneeDisp3_2], \
                'Верхняя граница оценки дисперсии': [VerhDisp1_2, VerhDisp2_2, VerhDisp3_2]}

# альфа = 0.01
data3 = {'Размер выборки':[50, 200, 1000], 'Нижняя граница оценки среднего': [NijneeSred1_3, NijneeSred2_3, NijneeSred3_3], \
        'Верхняя граница оценки среднего': [VerhSred1_3, VerhSred2_3, VerhSred3_3], \
            'Нижняя граница оценки дисперсии':[NijneeDisp1_3, NijneeDisp2_3, NijneeDisp3_3], \
                'Верхняя граница оценки дисперсии': [VerhDisp1_3, VerhDisp2_3, VerhDisp3_3]}



df1 = pa.DataFrame(data1, index = ['№1', '№2', '№3'])
df2 = pa.DataFrame(data2, index = ['№1', '№2', '№3'])
df3 = pa.DataFrame(data3, index = ['№1', '№2', '№3'])
with pa.ExcelWriter('Test_2.xlsx') as writer:  
    df1.to_excel(writer, sheet_name = 'Для alpa = 0.1')
    df2.to_excel(writer, sheet_name = 'Для alpa = 0.05')
    df3.to_excel(writer, sheet_name = 'Для alpha = 0.01')




# попытка в графики
'''
k = 1 + 3.322 * math.log(50)
k = 14 
# => bins = 14


def zakon(i):
    derf = []
    for t in range(i):
        d = (0.5**t/math.factorial(t))*math.exp(-0.5)
        derf.append(d)
    return derf
'''



cvcvc = [f"P{i}" for i in range(5)]
x = np.arange(len(cvcvc))
f1 = []
f2 = []
width = 0.3
for i in range(5):
    f1.append((v1.count(i)/50)) # массив вероятности по нашему массиву
    f2.append((0.5**i/math.factorial(i))*math.exp(-0.5)) # теоретическая вероятность по ф-ле из задания
fig, ax = plt.subplots()
''' это равносильно записи в цикле
f1.append((v1.count(0)/50))
f1.append((v1.count(1)/50))
f1.append((v1.count(2)/50))
f1.append((v1.count(3)/50))
f1.append((v1.count(4)/50))'''
#print(f1) проверяли действительно выводит вероятность возникновения конкретного числа в нашем полученном массиве с помощью ф-и Random...
rects1 = ax.bar(x - width/2, f1, width, label='Эмпирические значения', color = 'black') #в принципе .bar равносильно в hist параметру hitstype = 'bar'
rects2 = ax.bar(x + width/2, f2, width, label='Теоретические значения', color = 'pink')
ax.set_title('N = 50')
ax.set_xticks(x)
ax.set_xticklabels(cvcvc)
ax.legend()




f1 = []
''' заменили тем, что добавили эти иттерации в цикл
f1.append((v2.count(0)/200))
f1.append((v2.count(1)/200))
f1.append((v2.count(2)/200))
f1.append((v2.count(3)/200))
f1.append((v2.count(4)/200))'''
#print(f1) проверка как в первом случае
cvcvc = [f"P{i}" for i in range(5)]
x = np.arange(len(cvcvc))
f2 = []
width = 0.3
for i in range(5):
    f1.append((v2.count(i)/200))
    f2.append((0.5**i/math.factorial(i))*math.exp(-0.5)) #здесь мы задаём значения для теоретического закона распределения (смотрим вероятность по формуле, данной в условии)
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, f1, width, label='Эмпирические значения')
rects2 = ax.bar(x + width/2, f2, width, label='Теоретические значения')
ax.set_title('N = 200')
ax.set_xticks(x)
ax.set_xticklabels(cvcvc)
ax.legend()




f1 = []
'''заменили циклом как в первых двух случаях
f1.append((v3.count(0)/1000))
f1.append((v3.count(1)/1000))
f1.append((v3.count(2)/1000))
f1.append((v3.count(3)/1000))
f1.append((v3.count(4)/1000))'''
#print(f1) проверка
cvcvc = [f"P{i}" for i in range(5)]
x = np.arange(len(cvcvc))
f2 = []
width = 0.3
for i in range(5):
    f1.append((v3.count(i)/1000))
    f2.append((0.5**i/math.factorial(i))*math.exp(-0.5))
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, f1, width, label='Эмпирические значения', color = 'grey')
rects2 = ax.bar(x + width/2, f2, width, label='Теоретические значения', color = 'yellow')
ax.set_title('N = 1000')
ax.set_xticks(x)
ax.set_xticklabels(cvcvc)
ax.legend()
plt.show()