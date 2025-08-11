# 普通のfor文で偶数だけ集める
even = []
for n in [1, 2, 3, 4, 5]:
    if n % 2 == 0:
        even.append(n)

# リスト内包表記で書くとこう！
even = [n for n in [1, 2, 3, 4, 5] if n % 2 == 0]

# --- 課題① ---
# 以下の words の各文字列の長さをリストにして、lengths に代入しよう
# リスト内包表記を使ってね
words = ["apple", "banana", "orange"]
# 期待される出力: [5, 6, 6]
# ここにコードを書く
lengths = [len(word) for word in words]
print(lengths)

# --- 課題② ---
# 1〜20の中から、3の倍数だけを取り出してリストにしよう
# リスト内包表記 + range を使ってね
# 期待される出力: [3, 6, 9, 12, 15, 18]
# ここにコードを書く
multiples_of_three = [i for i in range(1,21) if i % 3 == 0]
print(multiples_of_three)

# --- 課題③ ---
# 以下の words の文字列をすべて大文字に変換して、新しいリストにしよう
# upper() を使って、リスト内包表記で書いてね
words = ["python", "java", "go"]
# 期待される出力: ["PYTHON", "JAVA", "GO"]
# ここにコードを書く
upper_words = [word.upper() for word in words]
print(upper_words)

# --- 応用課題① ---
# 1〜30までの数から、3の倍数は"Fizz"、5の倍数は"Buzz"、15の倍数は"FizzBuzz"、それ以外はそのままの数を
# 新しいリストにして変数 fizzbuzz_list に代入しよう
# ただしリスト内包表記を使って1行で書くこと

# 期待される出力例：
# [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', ...]

fizzbuzz_list = ["FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, 31)]
print(fizzbuzz_list)

# --- 応用課題② ---
# 以下のリスト names の中から、名前の長さが4文字以上のものだけを大文字にして新しいリストにしよう
names = ["Anna", "Bob", "Catherine", "David", "Eve"]
# 期待される出力: ['ANNA', 'CATHERINE', 'DAVID']

new_names = [word.upper() for word in names if len(word) >= 4]
print(new_names)

# --- 応用課題③ ---
# 以下の2つのリストから、同じインデックスにある要素を足したリストを作ろう
list1 = [10, 20, 30, 40]
list2 = [1, 2, 3, 4]
# 期待される出力: [11, 22, 33, 44]
# ヒント: zip() を使うよ

list3 = [value1 + value2 for (value1, value2) in zip(list1, list2)]
print(list3)
