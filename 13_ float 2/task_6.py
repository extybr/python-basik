print('Задача 6. Маятник ')

# Известно, что амплитуда качающегося маятника с каждым разом затухает
# на 8,4% от амплитуды прошлого колебания. 
# Если качнуть маятник,
# то, строго говоря, он не остановится никогда, 
# просто амплитуда будет постоянно уменьшаться до тех пор, 
# пока мы не сочтём такой маятник остановившимся. 
 
# Напишите программу, 
# определяющую, сколько раз качнётся маятник, прежде чем он, по нашему мнению, остановится. 
 
# Программа получает на вход
# начальную амплитуду колебания в сантиметрах 
# и конечную амплитуду его колебаний,
# которая считается остановкой маятника. 

# Обеспечьте контроль ввода.

# Пример:

# Введите начальную амплитуду: 1
# Введите амплитуду остановки: 0.1
 
# Маятник считается остановившимся через 27 колебаний

start_amplitude = float(input('Введите начальную амплитуду: '))
final_amplitude = float(input('Введите амплитуду остановки: '))
count = 0
if start_amplitude < final_amplitude:
    print('Ошибка ввода. Начальная амплитуда должна быть больше конечной')
else:
    while start_amplitude > final_amplitude:
        start_amplitude -= start_amplitude / 100 * 8.4
        count += 1
    print('Маятник считается остановившимся через', count, 'колебаний')