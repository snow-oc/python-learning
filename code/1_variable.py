age = 20 # int
height = 170.5 # float
name = "山田" # str
is_student = True # bool

print("年齢:", age)
print("身長:", height)
print("名前:", name)
print("学生ですか？", is_student)

print(type(age)) # <class 'int'>
print(type(height)) # <class 'float'>
print(type(name)) # <class 'str'>
print(type(is_student)) # <class 'bool'>

note_price = 250
print("ノートの4冊の金額は:", note_price * 4, "円です")

# f文字列
print(f"{name}さんの身長は{height}cmです。")
# 大文字、小文字
fruit1 = "Apple"
print(fruit1.upper())
print(fruit1.lower())
