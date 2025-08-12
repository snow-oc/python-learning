# --- 課題 ---
# 年齢を入力させて、18歳未満なら独自の例外を発生させるプログラムを作ろう
#
# 仕様:
# 1. UnderAgeError という例外クラスを作成（Exception クラスを継承）
# 2. 年齢を int で入力させる
# 3. 年齢が 18 未満なら UnderAgeError を発生させる
# 4. 各例外の処理内容
#    - UnderAgeError → 「18歳未満は利用できません」と表示
#    - ValueError → 「数字を入力してください」と表示
#    - その他のエラー → 「エラーが発生しました」と表示
# 5. finally で「処理終了」と表示
#
# ヒント:
# class UnderAgeError(Exception):
#     pass
#
# if age < 18:
#     raise UnderAgeError
class UnderAgeError(Exception):
    pass

try:
    age = int(input("年齢を入力してください: "))
    if age < 18:
        raise UnderAgeError("18歳未満は利用できません")
except UnderAgeError as e:
    print(e)
except ValueError:
    print("数字を入力してください")
except:
    print("エラーが発生しました")
finally:
    print("処理終了")
