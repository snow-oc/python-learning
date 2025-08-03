# --- 課題①: 名前のあいさつ関数 greet を作ろう ---
# 引数 name にデフォルト値 "ゲスト" を設定してね
# 実行例:
# greet()         → こんにちは、ゲストさん！
# greet("Tanaka") → こんにちは、Tanakaさん！
def greet(name="ゲスト"):
    print(f"こんにちは、{name}さん！")

greet()
greet("Tanaka")

# --- 課題②: 2つの数を受け取って、積（かけ算）を返す関数 multiply を作ろう ---
# 実行例:
# multiply(3, 4) → 12
def multiply(x, y):
    return x * y

print(multiply(3, 4))

# --- 課題③: 好きなだけ数を受け取って合計を返す関数 total を作ろう（*args を使おう！） ---
# 実行例:
# total(1, 2, 3) → 6
# total(10, 20, 30, 40) → 100
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))
print(total(10, 20, 30, 40))
