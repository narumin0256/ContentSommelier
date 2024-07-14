from flask import Flask, render_template, request
import openai  # openaiモジュールを正しくインポート
import os
from dotenv import load_dotenv
import json

load_dotenv()  # 環境変数をロード
openai.api_key = os.getenv('OPENAI_API_KEY')  # APIキーを設定

app = Flask(__name__)

mock_response = {
    "choices": [
        {
            "message": {
                "content": json.dumps({
                    "title": "進撃の巨人",
                    "genre": "アクション",
                    "summary": "巨人に立ち向かう人類の戦いを描く物語。",
                    "points": "緊迫感のあるストーリー展開と個性的なキャラクターが魅力。"
                })
            }
        }
    ]
}

def get_mock_response():
    return mock_response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    genre = request.form['genre']
    length = request.form['length']
    custom_genre = request.form.get('custom_genre')

    if genre == "custom":
        genre = custom_genre

    # # OpenAI APIを呼び出し
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "system", "content": "あなたは丁寧なギャルです."},
    #         {"role": "user", "content": f"ユーザー入力に基づいたおすすめの日本の漫画を教えてください: {user_input}"}
    #     ]
    # )

    response = get_mock_response()
    recommendation_content = response['choices'][0]['message']['content']
    recommendation = json.loads(recommendation_content)

    return render_template('result.html', recommendation=recommendation)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
