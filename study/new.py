import matplotlib.pyplot as plt

# Создаем данные для трех бизнесов
business1 = [10000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000]
business2 = [15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000]
business3 = [20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000]

# Создаем список лет и месяцев для оси x
x_axis = ['Jan 2021', 'Feb 2021', 'Mar 2021', 'Apr 2021', 'May 2021', 'Jun 2021', 'Jul 2021', 'Aug 2021', 'Sep 2021', 'Oct 2021']

# Создаем график с тремя линиями
plt.plot(x_axis, business1, label='Business 1')
plt.plot(x_axis, business2, label='Business 2')
plt.plot(x_axis, business3, label='Business 3')

# Добавляем заголовок и метки для осей
plt.title('Business Income Over Time')
plt.xlabel('Year and Month')
plt.ylabel('Income')

# Добавляем легенду для отображения линий, представляющих каждый бизнес
plt.legend()

# Отображаем график
plt.show()
