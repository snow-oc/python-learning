
# --- 課題① ---
# 以下の numbers を昇順（小さい順）に並び替えて、変数 sorted_numbers に代入しよう
numbers = [5, 2, 9, 1, 7]

# 期待される出力: [1, 2, 5, 7, 9]

# ここに書いてね
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# --- 課題② ---
# 以下の words を降順（ZからAの順）で並び替えて、変数 sorted_words に代入しよう
words = ["banana", "apple", "orange"]

# 期待される出力: ['orange', 'banana', 'apple']

# ここに書いてね
sorted_words = sorted(words, reverse=True)
print(sorted_words)

# --- 課題③ ---
# 以下の words を「文字列の長さが短い順」に並び替えて、変数 sorted_by_length に代入しよう
words = ["banana", "apple", "kiwi", "grape"]

# 期待される出力: ['kiwi', 'grape', 'apple', 'banana']

# ヒント: key に len を使うよ

# ここに書いてね
sorted_by_length = sorted(words, key=len)
print(sorted_by_length)

# --- 課題④ ---
# 以下の users を「ageの昇順」で並び替えて、新しいリスト sorted_users に代入しよう
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# 期待される出力:
# [
#     {"name": "Bob", "age": 25},
#     {"name": "Alice", "age": 30},
#     {"name": "Charlie", "age": 35}
# ]

# ヒント: key=lambda user: user["age"]

# ここに書いてね
sorted_users = sorted(users, key=lambda user: user["age"])
print(sorted_users)
