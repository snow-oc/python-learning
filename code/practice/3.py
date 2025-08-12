# --- 課題①（例外処理の応用）---
# ユーザーから2つの整数を入力し、それらを割り算するプログラムを作ってください。
# 条件:
# 1. 0で割った場合は「0では割れません」と表示
# 2. 数字以外が入力された場合は「数字を入力してください」と表示
# 3. どんな予期しないエラーでもキャッチして「エラーが発生しました」と表示
# 4. 最後に必ず「計算終了」と表示（finallyを使用）

# ヒント:
# - try-exceptをネストせず、exceptを複数使ってみよう
# - exceptの順番は重要（具体的な例外 → その他の例外）

# ここにコードを書く
try:
    input1 = int(input("数字1を入力してくだい: "))
    input2 = int(input("数字2を入力してください: "))
    result = input1 / input2
except ZeroDivisionError:
    print("0では割れません")
except ValueError:
    print("数字を入力してください")
except:
    print("エラーが発生しました")
finally:
    print("計算終了")
