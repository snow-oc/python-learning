# --- 応用課題① ---
# 以下の numbers から「偶数かつ3の倍数」の数字だけを抽出して、
# 新しいリスト even_and_multiple_of_3 に代入しよう
# filter() と lambda を使ってね
numbers = list(range(1, 31))
# 期待される出力: [6, 12, 18, 24, 30]

# ここにコードを書く
even_and_multiple_of_3 = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, numbers))
print(even_and_multiple_of_3)


# --- 応用課題② ---
# 以下の products から、「price が1000円以上」の商品だけを抽出して
# 新しいリスト expensive_products に代入しよう
# filter() を使ってね
products = [
    {"name": "pen", "price": 500},
    {"name": "notebook", "price": 1000},
    {"name": "bag", "price": 2500},
    {"name": "eraser", "price": 100}
]
# 期待される出力:
# [
#     {'name': 'notebook', 'price': 1000},
#     {'name': 'bag', 'price': 2500}
# ]

# ここにコードを書く
expensive_products = list(filter(lambda product: product["price"] >= 1000, products))
print(expensive_products)

# --- 応用課題③ ---
# 以下の emails から、「@example.com」で終わるメールアドレスだけを抽出して
# 新しいリスト example_emails に代入しよう
emails = [
    "john@example.com",
    "jane@gmail.com",
    "bob@example.com",
    "alice@yahoo.co.jp"
]
# 期待される出力:
# ['john@example.com', 'bob@example.com']

# ここにコードを書く
example_emails = list(filter(lambda email: email.endswith("@example.com") , emails))
print(example_emails)
