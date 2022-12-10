import numpy as np
import statistics


arr = np.arange(0, 88888888, 1, dtype = np.object)
print("Сумма ряда: ", arr.sum())
print("Среднее значение ряда: ", arr.mean())
rand_arr = (1000) * np.random.random_sample((100,))
print("Умножение ряда случайных чисел: ", rand_arr.prod())
print("Медиана случайного ряда: ", statistics.median(rand_arr))