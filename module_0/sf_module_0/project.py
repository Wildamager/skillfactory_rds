import numpy as np
def game_core_v3(number):
    predict=0
    count=0
    if 25<=number<50:predict+=np.random.randint(25,50)
    elif 0<=number<25:predict+=np.random.randint(1,25)
    elif 50<=number<75:predict+=np.random.randint(50,75)
    elif 75<=number<100:predict+=np.random.randint(75,100)   
    while number!= predict:
        count+=1
        if number > predict:predict+= 1
        elif number < predict:predict-= 1
    return(count)
def score_game(game_core_v3):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(int(game_core_v3(number)))
    score=np.mean(count_ls)
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
score_game(game_core_v3)