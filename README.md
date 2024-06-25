# README.md

## Languages
- [Japanese](#日本語)
- [English](#english)

## 日本語

### 概略
このリポジトリは、OpenAIのAPIを使用して、GPT-4モデルを利用するためのシンプルなPythonアプリケーションである。環境変数を使用してAPIキーを管理し、Dockerを使用してアプリケーションをコンテナ化している。世の中の無駄な複雑さを避け、シンプルに使えるように設計されている。

### 使用されている技術
| 技術         | バージョン  |
|--------------|--------------|
| Python       | 3.9-slim     |
| OpenAI API   | 最新         |
| python-dotenv| 最新         |
| Docker       | 最新         |
| Docker Compose | 最新       |

### 使用方法
1. リポジトリをクローンする
```bash
git clone https://github.com/clearclown/chatgpt-docker
cd chatgpt-docker
```

2. 必要な依存関係をインストールする
```bash
pip install -r requirements.txt
```

3. Dockerを使用してアプリケーションを実行する
```bash
docker-compose up --build
```


4. エラーや問題が発生した場合は、[issue](https://github.com/clearclown/chatgpt-docker/issues)に報告すること。

### Dockerの仕組み
Dockerは、アプリケーションをコンテナとしてパッケージ化し、どこでも一貫して動作させることができる技術である。`Dockerfile`には、ベースイメージの指定、作業ディレクトリの作成、必要なファイルのコピー、依存関係のインストール、スクリプトの実行が記述されている。`docker-compose.yml`は、複数のコンテナを一括で管理するための設定ファイルである。

### プロフィール
- [Twitter](https://www.x.com/arealnormalman) : @arealnormalman
- [Instagram](https://www.instagram.com/nm_a.normal.man/) : @nm_a.normal.man
- [LinkedIn](https://www.linkedin.com/in/arealnormalman/) : @arealnormalman

## English

### Overview
This repository contains a simple Python application that uses the OpenAI API to leverage the GPT-4 model. It manages API keys using environment variables and containerises the application using Docker. Designed to avoid the unnecessary complexities of the world, making it straightforward to use.

### Technologies Used
| Technology    | Version      |
|---------------|--------------|
| Python        | 3.9-slim     |
| OpenAI API    | Latest       |
| python-dotenv | Latest       |
| Docker        | Latest       |
| Docker Compose| Latest       |

### Usage
1. Clone the repository
```bash
git clone https://github.com/clearclown/chatgpt-docker
cd chatgpt-docker
```


2. Install the necessary dependencies
```bash
pip install -r requirements.txt
```

3. Run the application using Docker
```bash
docker-compose up --build
```

4. If any errors or issues arise, report them on [issue](https://github.com/clearclown/chatgpt-docker/issues).

### How Docker Works
Docker packages applications as containers, allowing them to run consistently anywhere. The `Dockerfile` specifies the base image, creates the working directory, copies necessary files, installs dependencies, and runs the script. The `docker-compose.yml` file is used to manage multiple containers at once.

### Profile
- [Twitter](https://www.x.com/arealnormalman) : @arealnormalman
- [Instagram](https://www.instagram.com/nm_a.normal.man/) : @nm_a.normal.man
- [LinkedIn](https://www.linkedin.com/in/arealnormalman/) : @arealnormalman

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.