# リスト
fruits = ["apple", "banana", "orange"]
print(fruits)

# 要素の取り出し（インデックスは0から）
print(fruits[0])  # apple
print(fruits[1])  # banana

# 要素の追加
fruits.append("grape")  # 最後に追加

# 要素の削除
fruits.remove("banana")

# 長さを調べる
print(len(fruits))

# ループで表示
for fruit in fruits:
    print(fruit)

# 練習問題②：リストと条件分岐
# 次のリストから「5より大きい数」だけを表示しよう。
numbers = [1, 3, 5, 7, 9, 2, 8]

for number in numbers:
    if number > 5:
        print(number)

# 練習問題③：リストの合計
# 次のリストの合計を求めて表示しよう。

scores = [10, 20, 30, 40, 50]

total = 0
for score in scores:
    total += score
print(total)

# 練習問題④：リストの最大値
# 次のリストの中で一番大きな数を表示しよう。

numbers = [3, 7, 2, 8, 5, 10, 6]

max_number = numbers[0]
for number in numbers:
    if max_number < number:
        max_number = number
print(max_number)

# 練習問題⑤：リストの中で偶数の数だけ合計する
# 次のリストの中から「偶数だけ」を取り出して合計を出してみよう

numbers = [1, 4, 7, 10, 12, 15, 18]

# ↓ここに処理を書こう
total = 0
for number in numbers:
    if number % 2 == 0:
        total += number

print(total)
