import random
answer = random.randint(100, 999)
i = 0

while i < 10:
    number = int(input('100~999の間の整数を入力してください：'))

    if answer == number:
        print(f'正解です! 答えは{answer}')
        break

    elif answer > number:
        print(f'不正解です。答えは、入力された値{number}よりも大きいです。')

    else:
        print(f'不正解です。答えは、入力された値{number}よりも小さいです。')

    i+=1