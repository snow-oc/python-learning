# --- 課題 ---
# 以下のリストから "a" を含む単語だけを新しいリストに入れて表示してね

words = ["apple", "banana", "cherry", "orange", "grape"]

# 実行結果の例:
# ['apple', 'banana', 'orange', 'grape']

new_words = []
keyword = "a"
for word in words:
    if keyword in word:
        new_words.append(word)
print(new_words)
