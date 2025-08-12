# --- 課題 ---
# ファイル操作と例外処理を組み合わせてみよう！
#
# 仕様:
# 1. "sample.txt" というファイルを開いて、その内容を表示する
# 2. ファイルが存在しない場合は「ファイルが見つかりません」と表示する
# 3. ファイル読み込み中に予期せぬエラーがあったら「エラーが発生しました」と表示する
# 4. 最後に必ず「処理終了」と表示する
#
# ヒント:
# - ファイルを開くときは open("sample.txt", "r") を使う
# - FileNotFoundError でファイルがない場合をキャッチ
# - except: で予期せぬエラーをキャッチ
# - finally: で必ず実行する処理を書く
# try:
#     file = open("sample.txt", "r")
#     content = file.read()
#     print(content)
#     file.close()
# except FileNotFoundError:
#     print("ファイルが見つかりません")
# except:
#     print("エラーが発生しました")
# finally:
#     print("処理終了")

try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("ファイルが見つかりません")
except:
    print("エラーが発生しました")
finally:
    print("処理終了")
