# 売上データ（辞書のリスト）
sales = [
    {"item": "apple", "price": 100, "quantity": 3},
    {"item": "banana", "price": 50, "quantity": 5},
    {"item": "orange", "price": 80, "quantity": 2},
    {"item": "apple", "price": 100, "quantity": 1},
    {"item": "banana", "price": 50, "quantity": 2},
]

# 課題①: 全体の売上金額を計算しよう
# それぞれのprice * quantityを足し合わせて total にしてね
total = 0
# ここに処理を書く
for sale in sales:
    amount = sale["price"] * sale["quantity"]
    total += amount
print(total)

# 課題②: 商品ごとの売上金額を集計しよう
# 例: {'apple': 400, 'banana': 350, 'orange': 160}
item_sales = {}
# ここに処理を書く
for sale in sales:
    item = sale["item"]
    amount = sale["price"] * sale["quantity"]
    if item in item_sales:
        item_sales[item] = item_sales[item] + amount
    else:
        item_sales[item] = amount
print(item_sales)

# 課題③: 一番売上が高かった商品を表示しよう
# 例: "最も売上が高い商品は banana で、売上は 350円です"
# ここに処理を書く
max_amount_item = {
    "name" : "",
    "amount": 0
}
for name, amount in item_sales.items():
    if amount > max_amount_item["amount"]:
        max_amount_item["name"] = name
        max_amount_item["amount"] = amount
print(f"最も売上が高い商品は {max_amount_item['name']} で、売り上げは {max_amount_item['amount']}円です")
