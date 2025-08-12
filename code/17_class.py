# クラスの例
class Person:
    def __init__(self, name, age):
        self.name = name # インスタンス変数
        self.age = age

    def greet(self): # メソッド
        print(f"こんにちは、私は{self.name}です。{self.age}歳です。")

p1 = Person("Alice", "25")
p1.greet()

# --- 課題① ---
# "Car" というクラスを作ってみよう
# 仕様:
# - 属性: brand（メーカー名）, model（車種）, year（年式）
# - メソッド: show_info() で「年式 ブランド モデル」という形式で表示する
#
# ヒント:
# 1. __init__() で3つのインスタンス変数を初期化
# 2. show_info() でprintを使ってフォーマットした文字列を出力
# 3. インスタンスを2台作って、それぞれshow_info()を呼び出す

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show_info(self):
        print(self.year, self.brand, self.model)

car1 = Car("ブランド1", "モデル1", "1980")
car2 = Car("ブランド2", "モデル2", "1990")
car1.show_info()
car2.show_info()

# --- 課題② ---
# 「Car」クラスを継承した「ElectricCar」クラスを作ろう
# ElectricCar は Car に加えて、バッテリー容量(battery_capacity)という属性を持つ
# show_info() メソッドをオーバーライドして
# 「年式 ブランド モデル バッテリー容量(kWh)」を表示するようにしよう

# ここに ElectricCar を作ってね
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year) # 親クラスのコンストラクタ
        self.battery_capacity = battery_capacity

    def show_info(self):
        print(self.year, self.brand, self.model, self.battery_capacity)

# ElectricCar のインスタンスを作って show_info() を呼び出してみよう
electric_car = ElectricCar("ブランド3", "モデル3", "2000", 8000)
electric_car.show_info()
