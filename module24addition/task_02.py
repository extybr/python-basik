""" Задача 2. Однотипные объекты

В офис заказали небольшую партию из четырёх мониторов и трёх наушников.
У монитора есть четыре характеристики: название производителя, матрица,
разрешение и частота обновления экрана. Все четыре монитора отличаются
только частотой.

У наушников три характеристики: название производителя, чувствительность
и наличие микрофона. Отличие только в наличии микрофона. """

class Monitor:
    monitor_name = 'Samsung'
    monitor_matrix = 'VA'
    monitor_res = 'WQHD'
    monitor_freq = 60


class Headphones:
    headphones_name = 'Sony'
    headphones_sensitivity = 108
    headphones_micro = False


monitor_1 = Monitor()

monitor_2 = Monitor()
monitor_2.monitor_freq = 144

monitor_3 = Monitor()
monitor_3.monitor_freq = 70

monitor_4 = Monitor()
monitor_4.monitor_freq = 60

headphones_1 = Headphones()

headphones_2 = Headphones()
headphones_2.headphones_micro = True

headphones_3 = Headphones()
headphones_3.headphones_micro = True

print(headphones_3.headphones_name)
