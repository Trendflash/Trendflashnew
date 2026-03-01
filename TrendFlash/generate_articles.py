import os
import json
from datetime import datetime

try:
    from openai import OpenAI
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
except ImportError:
    client = None
    print("OpenAIモジュールがありません。サンプル記事を生成します。")

JSON_FILE = "articles.json"
ARTICLES_DIR = "articles"
os.makedirs(ARTICLES_DIR, exist_ok=True)

def create_article():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            articles = json.load(f)
    else:
        articles = []

    if client:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "TrendFlash用の記事を1件生成してください"}]
        )
        content = response.choices[0].message.content
    else:
        content = "これはサンプル記事です。自動更新テスト用。"

    article_num = len(articles) + 1
    title = f"新記事 {article_num}"

    articles.append({
        "title": title,
        "link": f"{ARTICLES_DIR}/article{article_num}.html",
        "content": content,
        "date": datetime.now().isoformat()
    })

    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

    html_filename = os.path.join(ARTICLES_DIR, f"article{article_num}.html")
    with open(html_filename, "w", encoding="utf-8") as f:
        f.write(f"<html><body><h1>{title}</h1><p>{content}</p><small>{datetime.now().isoformat()}</small></body></html>")

    print(f"{html_filename} を生成しました。記事 {article_num} 件")

if __name__ == "__main__":
    create_article()