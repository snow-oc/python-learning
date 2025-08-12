# 課題:
# 1. greet() 関数を持つ mymodule.py を作ってください（引数の名前に挨拶する）
# 2. main.py からその greet() を呼び出してください
# 3. my_package というパッケージを作り、そこに say_hello() を持つ module1.py を置き、
#    main.py から呼び出してください
# import mymodule
from my_package import module1

# mymodule.greet("太郎")
module1.say_hello()
