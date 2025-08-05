# --- 関数の基本 ---

# 課題①: 挨拶をする関数を作って呼び出してみよう
# 期待される出力: こんにちは！
def say_hello():
    print("こんにちは！")

say_hello()

# 課題②: 名前を受け取って、挨拶する関数を作ろう
# 期待される出力（引数に "たろう" を渡した場合）: こんにちは、たろうさん！
def greet(name):
    print(f"こんにちは、{name}さん！")

greet("たろう")

# 課題③: 2つの数を足して返す関数を作ろう（戻り値を使う）
# 期待される出力（引数に 3 と 5 を渡した場合）: 8
def add(a, b):
    return a + b

print(add(3, 5))

# 課題④: リストの合計値を計算する関数を作ってみよう
# ヒント: forループを使って1つずつ足していこう
# 期待される出力: 15 （例: [1, 2, 3, 4, 5] の合計）
def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum_list([1, 2, 3, 4, 5]))

# --- 関数の応用練習 ---

# 課題①: 渡されたリストの中に偶数がいくつあるか数えて返す関数を作ろう
# 期待される出力: 3 （例: [1, 2, 4, 5, 6] の場合）
def count_even(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count

print(count_even([1, 2, 4, 5, 6]))

# 課題②: 渡されたリストの中で最大の値を返す関数を作ろう
# ※組み込み関数 max() は使わず、自力で実装してね！
def find_max(numbers):
    max_num = numbers[0]
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num

print(find_max([3, 10, 7, 1]))

# --- 課題①: 偶数かどうかを判定する関数を作ろう ---
# 引数で受け取った数が偶数なら True、奇数なら False を返す

def is_even(n):
    return n % 2 == 0


# --- 課題②: リストの中で偶数だけを集めて新しいリストを返す関数を作ろう ---
# 例: [1, 2, 3, 4] → [2, 4]

def filter_even(numbers):
    new_numbers = []
    for n in numbers:
        if n % 2 == 0:
            new_numbers.append(n)
    return new_numbers


# --- 課題③: 課題①の関数を②の中で使ってね！（関数の中で関数を使う！） ---
# 結果を print() で表示してみよう
def filter_even2(numbers):
    even_numbers = []
    for n in numbers:
        if is_even(n):
            even_numbers.append(n)
    return even_numbers

print(filter_even2([1, 2, 3, 4]))
