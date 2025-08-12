# 例1
try:
    result = 10 / 0
except ZeroDivisionError:
    print("0で割ることはできません")

# 例2
try:
    number =int(input("数字を入力してください: "))
    result = number / 0
except ValueError:
    print("数字を入力してください")
except ZeroDivisionError:
    print("0で割ることはできません")

# 例3
try:
    f = open("test.txt", "r")
except FileNotFoundError:
    print("ファイルが見つかりません")
finally:
    print("処理が完了しました")
