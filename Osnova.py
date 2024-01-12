"Марковские цепи"
import numpy as np
import pandas as pd 
from sklearn import preprocessing 
from markovchain import MarkovChain 
import random
import matplotlib.pyplot as plt
#генерация матрицы переходов P и матрица вероятностей 
#P=[0.8 ,0.1, 0.1, 0, 0.2, 0.7, 0.1, 0, 0.1, 0.2, 0.5, 0.2, 0.2, 0.2, 0.2, 0.4 ] #коэффициенты матрицы переходных вероятностей
p = np.array([[0.8 ,0.1, 0.1, 0],
                   [0.2, 0.7, 0.1, 0],
                   [0.1, 0.2, 0.5, 0.2],
                   [0.2, 0.2, 0.2, 0.4]])
#нормировка
p_norm = preprocessing.normalize(p) # тут ниче не работает, плохая функция

def normalize(transitions,n):
    matrix = np.reshape(transitions, (n, n))
    arr = np.array([])
    for row in matrix:
        row = row / sum(row)
        arr = np.append(arr, row)
    prop = np.reshape(arr, (n, n))
    return(prop)

#сумма меньше 1
print(sum(p_norm[0]))
print(sum(p_norm[1]))
print(sum(p_norm[2]))
print(sum(p_norm[3]))
#график 
'''
p = np.array([[0.8 ,0.1, 0.1, 0],
                   [0.2, 0.7, 0.1, 0],
                   [0.1, 0.2, 0.5, 0.2],
                   [0.2, 0.2, 0.2, 0.4]])'''
p_norm = normalize(p, 4)
mc= MarkovChain(p_norm, ['Healthy','Unwell','Sick' ,'Very sick'])
mc.draw("D:\ЛЭТИ\Цифровая кафедра\markov-chain-four-states.png")

# кумулятивная матрица, пункт 4
p_cum = np.cumsum(p_norm, axis = 1)
#print(p_norm)
#print(p_cum)


# попытки в моделирование. пункт 5. хз хз хз
'''
zt = [1]
for i in range(0, 199):
    for j in range(200):
        
        zt[i+1] = sum(random.random()) '''

# функция прогноза???????????, пункт 5 всё ещё
def prognoz_pogodi(p_cum, n):
    r = np.array([random.random() for i in range(n)])
    z = []
    for i in range(n):
        k = 0
        if i == 0:
            z.append(1)
        else:
            while r[i-1] >= p_cum[z[i-1], k]:
                k = k + 1
            else:
                z.append(k)
    return(z)

# нам дали три кучки камней (200, 1000, 10000), мы из них что-то делаем
plt.subplot(3, 1, 1)
prg1 = prognoz_pogodi(p_cum, 200)
plt.plot(prg1)
plt.ylim(0, 3)
plt.title('Поведение цепи Маркова для N = 200')

plt.subplot(3, 1, 2)
prg2 = prognoz_pogodi(p_cum, 1000)
plt.plot(prg2)
plt.ylim(0, 3)
plt.title('Поведение цепи Маркова для N = 1000')

plt.subplot(3, 1, 3)
prg3 = prognoz_pogodi(p_cum, 10000)
plt.plot(prg3)
plt.ylim(0, 3)
plt.title('Поведение цепи Маркова для N = 10000')
plt.show()

# теперь мы оцениваем цепь Маркова
# функция суперской оценки цепи маркова, пункт 9, хотя вообще 8, но ладно
def klassnaya_funkcia_obs(z):
    p_obs = np.zeros((4, 4), dtype=float)
    N = len(z)
    for n in range(0, N):
        for i in range(4):
            if z[n-1] == i+1:
                for j in range(4):
                    if z[n] == j+1:
                        p_obs[i, j] = p_obs[i, j]+1
                        #print(p_obs)
    return(p_obs)


x1 = klassnaya_funkcia_obs(prg1)
p1 = normalize(x1, 4)

mc = MarkovChain(p1, ['Healthy', 'Unwell','Sick','Very sick'])
mc.draw()
p_cum1 = np.cumsum(p1, axis = 1)
print(p1)
print(p_cum1)



x2 = klassnaya_funkcia_obs(prg2)
p2 = normalize(x2, 4)

mc = MarkovChain(p2, ['Healthy', 'Unwell','Sick','Very sick'])
mc.draw()
p_cum2 = np.cumsum(p2, axis = 1)
print(p2)
print(p_cum2)



x3 = klassnaya_funkcia_obs(prg3)
p3 = normalize(x3, 4)
mc = MarkovChain(p3, ['Healthy', 'Unwell','Sick','Very sick'])
mc.draw()
p_cum3 = np.cumsum(p3, axis = 1)
print(p3)
print(p_cum3)



#добивочка, 10 пункт
plt.subplot(2, 1, 1)
prg1 = prognoz_pogodi(p_cum, 200)
plt.plot(prg1)
plt.ylim(0, 5)
plt.title('Поведение цепи Маркова для N = 200')

plt.subplot(2, 1, 2)
l = prognoz_pogodi(p_cum1, 200)
plt.plot(l)
plt.ylim(0, 5)
plt.title('Поведение цепи Маркова для N = 200 (оценка)')

plt.show()


