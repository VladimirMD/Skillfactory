import numpy as np
import  math
# Подключаем библиотеку для использования метода math.ceil
def score_game(game_core):

    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


def game_core_v2(number):


    count = 1
    predict = 50 #Середина диапазона поиска
    span=predict/2 #Дополнительная переменная для сохранения изменений интервала


    while number != predict:
        count += 1
        if number > predict:
            predict += span
            span = math.ceil(span/2)
        elif number < predict:
            predict -= span
            span = math.ceil(span/2)

    return(count)  # выход из цикла, если угадали


print(score_game(game_core_v2))
