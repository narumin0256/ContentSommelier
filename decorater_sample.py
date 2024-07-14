from flask import Flask, render_template

#FlaskアプリケーションのインスタンスをFlaskクラスから作成
app = Flask(__name__)

def my_decorator(func):
    def wrapper(*args, **kwargs):
        #引数の関数を実行する前の処理
        print("Before the function call")

        #引数の関数を実行
        result = func(*args, **kwargs)

        #引数の関数を実行した後の処理
        print("After the function call")

        return result
    return wrapper

@my_decorator
def say_hello(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


say_hello("Alice")
say_hello("Bob", greeting="Hi")



