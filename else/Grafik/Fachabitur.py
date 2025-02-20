import matplotlib.pyplot as plt
import numpy as np

# Данные из задачи
r_cm = np.array([7.0, 8.0, 10.0, 14.0])  # расстояние в см
E_kVm = np.array([10.3, 9.0, 7.2, 5.1])  # напряжённость в кВ/м

# Вычисляем 1/r для оси X
inv_r = 1 / r_cm

# Строим график
plt.figure(figsize=(8, 5))
plt.plot(inv_r, E_kVm, 'o-', label='Измеренные данные', markersize=8, color='blue')

# Подписи осей
plt.xlabel(r'$1/r$ (в 1/см)', fontsize=12)
plt.ylabel(r'$E$ (в кВ/м)', fontsize=12)

# Заголовок и сетка
plt.title('Зависимость E от 1/r', fontsize=14)
plt.grid(True)

# Легенда
plt.legend(loc='best')

# Отображение графика
plt.show()