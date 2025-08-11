# --- 課題① ---
# 以下の2つのリスト name_list と score_list を使って、
# 「名前: 点数」という形式の文字列にして新しいリストにしよう
# ヒント: zip() を使うよ
name_list = ["Alice", "Bob", "Charlie"]
score_list = [85, 92, 78]

# 期待される出力: ['Alice: 85', 'Bob: 92', 'Charlie: 78']

# ここにコードを書く
score_name_list = [ name + ":" + str(score) for name, score in zip(name_list, score_list)]
print(score_name_list)

# --- 課題② ---
# 以下の2つのリスト words1 と words2 を使って、
# 同じインデックスの単語をスペースで結合した新しいリストを作ろう
# ヒント: zip() を使って文字列を " ".join([word1, word2]) でもOK
words1 = ["good", "nice", "great"]
words2 = ["morning", "job", "work"]

# 期待される出力: ['good morning', 'nice job', 'great work']

# ここにコードを書く
join_word_list = [f"{word1} {word2}" for word1, word2 in zip(words1, words2)]
print(join_word_list)

# --- 応用課題 ---
# 以下の2つのリスト list1 と list2 を使って、
# 同じインデックスの要素をタプルにして、タプルのリストを作ろう
# さらに、そのリストの中から「2つの値の合計が100以上」のタプルだけを抽出しよう
list1 = [60, 40, 90, 30]
list2 = [50, 70, 20, 80]

# 期待される出力: [(60, 50), (40, 70), (30, 80)]

# ここにコードを書く
join_list = list(zip(list1, list2))
join_list = list(filter(lambda x: x[0] + x[1] >= 100, join_list))
print(join_list)
