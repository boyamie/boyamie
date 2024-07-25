import feedparser
import time
import os

# RSS 피드 URL
RSS_URL = "https://velog.io/@boyamie_/posts"  # 실제 RSS 피드 URL로 변경하세요

# RSS 피드에서 항목을 가져옵니다.
RSS_FEED = feedparser.parse(RSS_URL)

# 최대 포스트 수 설정
MAX_POST = 5

# README.md 파일의 기존 내용을 읽습니다.
readme_path = "README.md"
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        existing_content = f.read()
else:
    existing_content = ""

# 새로운 Markdown 텍스트 초기화
new_posts = "\n## 📝 Latest Posting\n"

# 블로그 게시물 추가
for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    feed_date = feed['published_parsed']
    new_posts += f"- [{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']})  \n"

# 기존 내용에서 기존 최신 포스트 부분을 제거하고 새로운 포스트 부분을 추가합니다.
start_marker = "## 📝 Latest Posting"
if start_marker in existing_content:
    existing_content = existing_content.split(start_marker)[0]

# README.md 파일에 기존 내용과 새로운 내용을 함께 씁니다.
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(existing_content + new_posts)
