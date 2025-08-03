# 辞書の作成
person = {
    "name": "Tanaka",
    "age": 20,
    "city": "Tokyo"
}

# 値の取得
print(person["name"])

# 値の更新
person["age"] = 31

# 要素の追加
person["job"] = "Engineer"

# 要素の削除
del person["city"]

# 辞書のループ
for key, value in person.items():
    print(key, "→", value)

# 課題①: 自分のプロフィールを辞書で作ろう（name, age, hobby など）
profile = {
    "name": "Yamamoto",
    "age": 30,
    "hobby": "game"
}

# 課題②: hobby を "読書" に更新してみよう
profile["hobby"] = "読書"
print(profile["hobby"])

# 課題③: 新しく "favorite_language" というキーを追加して、"Python" を入れてみよう
profile["favorite_language"] = "Python"

# 課題④: プロフィールの内容をすべてループして表示しよう
for key, value in profile.items():
    print(key, ":", value)
