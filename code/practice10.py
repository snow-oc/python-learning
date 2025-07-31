# while文を使って、1から10までの偶数だけ表示しよう！
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        print(i)

# 変数 total を 0 にして、1から順に数字を足していこう
# 合計が100を超えたらループを終わらせて、最後の合計を表示しよう！
total = 0
i = 1
while True:
    total += i
    if total >= 100:
        print(total)
        break
    i += 1

# input() を使ってユーザーの入力を受け取ろう
# ユーザーが「exit」と入力したらループを抜けるようにしよう！
user_input = ""
while user_input != "exit":
    user_input = input("文字を入力してください:")
    print(f"入力した文字列:{user_input}")
print("チャット終了")
