# --- 課題① ---
# 以下の numbers から3の倍数だけを取り出して、変数 multiples_of_3 に代入しよう
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# 期待される出力: [3, 6, 9, 12]

# ここに書いてね
multiples_of_3 = list(filter(lambda x : x % 3 == 0, numbers))
print(multiples_of_3)


# --- 課題② ---
# 以下の words から、5文字以上の単語だけを取り出して新しいリストにしよう
words = ["apple", "banana", "kiwi", "grape", "pear"]
# 期待される出力: ['apple', 'banana', 'grape']

# ここに書いてね
words_filter = list(filter(lambda x: len(x) >= 5, words))
print(words_filter)


# --- 課題③ ---
# 以下の users から、age が 30 未満のユーザーだけを抽出して新しいリストにしよう
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 22}
]
# 期待される出力:
# [{'name': 'Bob', 'age': 25}, {'name': 'David', 'age': 22}]

# ここに書いてね
users_filter = list(filter(lambda user: user["age"] < 30, users))
print(users_filter)
