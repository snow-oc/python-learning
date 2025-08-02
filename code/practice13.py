# 課題①: 複数人のプロフィールを辞書のリストで定義しよう
people = [
    {"name": "Yamamoto", "age": 30, "hobby": "読書"},
    {"name": "Tanaka", "age": 25, "hobby": "映画"},
    {"name": "Sato", "age": 40, "hobby": "旅行"}
]

# 課題②: 全員の名前を表示しよう
# 期待される出力:
# Yamamoto
# Tanaka
# Sato

for person in people:
    print(person["name"])

# 課題③: 年齢が30歳以上の人だけ表示しよう
# 出力形式:
# Yamamoto は 30歳です
# Sato は 40歳です
for person in people:
    if person["age"] >= 30:
        print(f"{person['name']} は {person['age']}歳です")

# 課題④: 全員の hobby を「ゲーム」に変更しよう（ループを使って）
for person in people:
    person["hobby"] = "ゲーム"

# 課題⑤: 最終的な people の中身をすべて表示してみよう
# keyとvalueを使って1人ずつ表示する
for person in people:
    for key, value in person.items():
        print(key, value)
