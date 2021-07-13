import numpy as np


def search(number):
    predict = list(range(1, 101)) #опрееляем список из 100 элементов
    left = 1 # левая граница поиска
    right = 100 # правая граница поиска
    result = 0 #результат нахождения
    count = 1 # количество попыток
    while (left <= right) and (result == 0): #пока права граница больше левой и результат не найден
        mid = (left+right)//2 # находим середину списка
        if predict[mid] == number: # если это число искомое число, то записываем в результат
            result = mid
        else:
            if number<predict[mid]: #если середина больше искомого числа, то правой граничей становится число на одно меньшее середины
                right = mid -1
            else: #если середина меньше искомого числа, то левой граничей становится число на одно большее середины
                left = mid +1
        count += 1 #считаем попытки
    return count

def score_game():
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(search(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game()
