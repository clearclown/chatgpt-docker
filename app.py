import os
from openai import OpenAI
from dotenv import load_dotenv

# 環境変数をロード
load_dotenv()

def get_gpt_response(prompt):
    try:
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="gpt-4o",
            max_tokens=300,
        )
        # レスポンスの内容をログに出力
        print("Response object:", response)

        # 正しいフィールドを参照してレスポンスを取得
        message_content = response.choices[0].message.content.strip()
        return message_content

    except openai.error.OpenAIError as e:
        # OpenAIのエラーを詳細にログ出力
        print(f"OpenAI API error: {e}")
        return f"OpenAI API error: {e}"
    except KeyError as e:
        # レスポンスオブジェクトに期待するキーが存在しない場合のエラーをログ出力
        print(f"Key error: {e}")
        return f"Key error: {e}"
    except AttributeError as e:
        # 属性エラーを詳細にログ出力
        print(f"Attribute error: {e}")
        return f"Attribute error: {e}"
    except Exception as e:
        # その他の予期しないエラーを詳細にログ出力
        print(f"An unexpected error occurred: {e}")
        return f"An unexpected error occurred: {e}"

if __name__ == "__main__":
    prompt = "say 「Hello World」 in Arabic"
    response = get_gpt_response(prompt)
    print("AIの応答:")
    print(response)
