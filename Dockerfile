# ベースイメージを指定
FROM python:3.9-slim

# 作業ディレクトリを作成
WORKDIR /app

# 必要なファイルをコピー
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY .env .env

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# スクリプトを実行
CMD ["python", "app.py"]
