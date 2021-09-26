import random

i = 4
j = 1

random_number = random.randint(1, 20)


while i > 0:
    number = int(input(f"기회가 {i}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요:")) # you have i chances left, guess number between 1, 20
    if number == random_number:
        print(f'축하합니다. {j}번만에 숫자를 맞히셨습니다.') # congratulation. you've guessed right in j tries
        break
    elif number < random_number:
        print('UP')
        i -= 1
        j += 1
    else:
        print('DOWN')
        i -= 1
        j += 1
        if i == 0:
            print(f'아쉽습니다. 정답은 {random_number}였습니다.') #We are sorry. The answer was random_number 
