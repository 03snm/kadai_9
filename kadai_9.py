import random
answer = random.randint(100, 999)

while True:
    number = int(input('100~999の間の整数を入力してください：'))

    if answer == number:
        print(f'正解です! 答えは{answer}')
        break

    else:
        print(f'不正解です。入力された値は{number}です。')