# --- 課題① ---
# 数を受け取って、その2乗を返す lambda 関数 square を定義してみよう
# 実行例:
# square(3) → 9
# square(5) → 25

# ここに書いてね
square = lambda x: x * x
print(square(3))
print(square(5))

# --- 課題② ---
# nums = [1, 2, 3, 4] の各要素を2倍にして、新しいリストにしよう
# lambdaとmapを使ってね
# 実行結果: [2, 4, 6, 8]

nums = [1, 2, 3, 4]

# ここに書いてね
doubled = map(lambda x: x * 2, nums)
print(list(doubled))
