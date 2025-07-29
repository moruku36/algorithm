null = 0
import random

answer = random.randint(1, 20)

print("1から20の数字を当ててください！")

while True:
    guess = input("あなたの予想: ")

    if not guess.isdigit():
        print("数字を入力してください。")
        continue

    guess = int(guess)

    if guess == answer:
        print("正解です！🎉")
        break
    elif guess < answer:
        print("もっと大きいです。")
    else:
        print("もっと小さいです。")