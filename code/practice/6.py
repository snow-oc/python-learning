# 【課題】ファイルへの書き込み＋読み込み（例外処理付き）
# 1. sample.txt に好きな文章を書き込む（write）
# 2. 書き込んだファイルを開いて内容を読み込んで表示する（read）
# 3. ファイルが見つからない場合は FileNotFoundError をキャッチ
# 4. その他のエラーは汎用 except で「エラーが発生しました」と表示
# 5. 最後に「処理終了」と表示

# ヒント：
# with open("ファイル名", "モード", encoding="utf-8") as f:
#   モード:
#     "w" → 書き込み（既存の内容を消して書く）
#     "r" → 読み込み
#     "a" → 追記
try:
    with open("sample.txt", "w", encoding="utf-8") as f:
        f.write("テスト")
    with open("sample.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("ファイルが見つかりません")
except:
    print("エラーが発生しました")
finally:
    print("処理終了")
