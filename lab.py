import numpy as np 
import matplotlib.pyplot as plt 
f = lambda x: 2**x 
N = 10 # количество интервалов разбиения 
left_bound = 0 # пределы интегрирования 
right_bound = 1
method = 'center' # left center or right 

lenght = right_bound - left_bound # длина отрезка, на котором интегрируем 
step = lenght / N 

ans = 0 


# графики иуууууу 
fig = plt.figure() 
ax = fig.add_subplot(1, 1, 1)
x = np.linspace(left_bound-0.5, right_bound+0.5, N)
ax.plot(x, f(x)) # русуем график функции 
ax.axvline(left_bound, ls = '--', color = 'red')
ax.axvline(right_bound, ls = '--', color = 'red')


xi = lambda i: left_bound + step * i if method == 'left' else left_bound + step * i + step / 2  if method == 'center' else left_bound + step * (i + 1)

# считаем интегральную сумму и рисуем прямоугольники 
for i in range(N):
    ans += f(xi(i)) * step 
    ax.bar(left_bound + step * i, f(xi(i)), step, align = 'edge', edgecolor='purple', color='lightgray')


print(ans)


plt.show()