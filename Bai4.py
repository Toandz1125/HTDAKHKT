import random
import time

words = ["python", "apple", "river"]

secret_word = random.choice(words)
guessed = ["_"] * len(secret_word)

wrong_turns = 5
used_letters = []

start_time = time.time()

print("Từ bí mật:", " ".join(guessed))

while wrong_turns > 0 and "_" in guessed:
    guess = input("Nhập chữ cái: ").lower()

    if guess in used_letters:
        print("Bạn đã nhập chữ này rồi!")
        continue

    used_letters.append(guess)

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed[i] = guess
        print("Đúng:", " ".join(guessed))
    else:
        wrong_turns -= 1
        print(f"Sai! Còn {wrong_turns} lượt")

if "_" not in guessed:
    result = "Thắng"
    print("Chúc mừng! Bạn đã thắng")
else:
    result = "Thua"
    print("Bạn thua! Từ đúng là:", secret_word)

end_time = time.time()
time_used = round(end_time - start_time, 2)

with open("game_result.txt", "a", encoding="utf-8") as file:
    file.write("----- Lượt chơi mới -----\n")
    file.write(f"Từ bí mật: {secret_word}\n")
    file.write(f"Kết quả: {result}\n")
    file.write(f"Thời gian chơi: {time_used} giây\n")
    file.write(f"Số lượt sai còn lại: {wrong_turns}\n\n")

print("Đã lưu kết quả vào file game_result.txt")