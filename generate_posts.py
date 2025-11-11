import pandas as pd
from datetime import datetime
import os
import re

# ==============================================================================
# 설정: CSV 파일 경로, 폴더, 날짜 형식, 작성자별 색상 매핑
# ==============================================================================
CSV_FILE_PATH = '블로그 스케줄 23e55850f3a480309f95d7603c8f79ae.csv'
POSTS_DIR = 'example/_posts'  # 게시물 파일이 저장될 폴더
DATE_FORMAT_IN_CSV = r'(\d{4})년 (\d{1,2})월 (\d{1,2})일'  # CSV 파일의 날짜 형식 정규식

# Jekyll의 기본 Permalink 구조를 가정 (예: /YYYY/MM/DD/post-slug/)
BASE_URL_FORMAT = "/{}/{}/{}/{}/" 

# 작성자 이름과 매칭될 CSS 클래스 및 HEX 코드 정의
AUTHOR_COLOR_CLASSES = {
    '김강연': 'author-blue',
    '장진욱': 'author-green',
    '정수민': 'author-purple',
    '배재유': 'author-navy',
    '김민재': 'author-orange'
}
AUTHOR_COLOR_HEX = {
    'author-blue': '#007bff',
    'author-green': '#28a745',
    'author-purple': '#6f42c1',
    'author-navy': '#001f3f',
    'author-orange': '#fd7e14',
    'author-default': '#333333'
}

# ==============================================================================
# 함수 정의
# ==============================================================================

def create_jekyll_post(row):
    """CSV 한 행의 데이터를 Jekyll 포스트 파일로 생성하고 토글 구조를 추가합니다."""
    
    # 1. 데이터 파싱
    post_title = str(row['게시물 이름']).strip()
    author = str(row['게시자']).strip()
    topics = str(row['주제']).strip()
    
    if not post_title:
        print(f"⚠️ 경고: 게시물 이름이 비어있어 해당 행을 스킵합니다.")
        return

    date_match = re.search(DATE_FORMAT_IN_CSV, str(row['게시일']))
    if not date_match:
        print(f"⚠️ 경고: '{post_title}' 게시물의 날짜 형식을 인식할 수 없습니다. 스킵합니다.")
        return

    year, month, day = date_match.groups()
    post_date = datetime(int(year), int(month), int(day))

    # 2. 파일명 및 링크 생성
    slug = re.sub(r'[^\w\s-]', '', post_title).strip().replace(' ', '-').lower()
    
    # 파일명 형식: YYYY-MM-DD-[작성자]-[게시글-슬러그].md
    filename_slug = re.sub(r'[^\w\s-]', '', author).strip().replace(' ', '-') + '-' + slug
    filename = f"{post_date.strftime('%Y-%m-%d')}-{filename_slug}.md"
    
    filepath = os.path.join(POSTS_DIR, filename)

    # Jekyll 게시글 URL 생성
    post_url = BASE_URL_FORMAT.format(
        post_date.strftime('%Y'), 
        post_date.strftime('%m'), 
        post_date.strftime('%d'), 
        filename_slug
    )

    # 3. Front Matter (YAML 헤더) 생성
    tags_list = [t.strip() for t in topics.split(',') if t.strip()]
    category = tags_list[0] if tags_list else '미분류'
    
    front_matter = f"""---
layout: post
title: "{post_title}"
author: "{author}"
date: {post_date.strftime('%Y-%m-%d 00:00:00 +0900')}
categories: [{category}]
tags: {tags_list}
---

"""
    # 4. Markdown 본문 내용 추가 (토글 및 링크 구조 개선)
    
    author_class = AUTHOR_COLOR_CLASSES.get(author, 'author-default')
    author_hex = AUTHOR_COLOR_HEX.get(author_class, '#333333')
    date_str = post_date.strftime('%Y년 %m월 %d일')
    
    # 본문에는 게시글 제목 대신 토글 구조만 깔끔하게 남깁니다.
    post_content = f"""
<div style="border: 1px solid #ddd; padding: 15px; margin-bottom: 20px; border-radius: 5px;">
    
    <details>
        <summary style="cursor: pointer; font-size: 1.1em; font-weight: bold; color: {author_hex}; margin-bottom: 5px;">
            <span style="font-size: 1.2em;">👉</span> 
            {author}의 게시물 목록 (클릭하여 펼치기)
        </summary>
        
        <div style="padding: 10px 0 0 10px; font-size: 0.95em;">
            
            <p style="margin-bottom: 5px;">
                <strong>게시글:</strong> 
                <a href="{post_url}" target="_blank" style="text-decoration: none; font-weight: bold; color: {author_hex};">
                    {post_title}
                </a>
            </p>
            <p style="margin-top: 5px;"><strong>게시 예정일:</strong> {date_str}</p>
            <p style="margin-top: 5px;"><strong>주요 주제:</strong> {topics if topics else '미지정'}</p>
        </div>
    </details>
</div>

"""
    final_content = front_matter + post_content

    # 5. 파일 저장
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"✅ 파일 생성 완료: {filepath}")
    except Exception as e:
        print(f"❌ 파일 생성 실패 ({filepath}): {e}")


def main():
    """메인 함수: CSV를 로드하고 포스트 생성을 시작합니다."""
    
    # _posts 폴더가 없으면 생성
    os.makedirs(POSTS_DIR, exist_ok=True)

    try:
        df = pd.read_csv(CSV_FILE_PATH, encoding='utf-8')
    except FileNotFoundError:
        print(f"❌ 오류: 파일을 찾을 수 없습니다: {CSV_FILE_PATH}")
        return
    except UnicodeDecodeError:
        print("❌ 오류: CSV 파일 인코딩 문제. 'euc-kr'로 재시도합니다.")
        try:
            df = pd.read_csv(CSV_FILE_PATH, encoding='euc-kr')
        except Exception as e:
            print(f"❌ 오류: euc-kr 로드도 실패했습니다: {e}")
            return
    except Exception as e:
        print(f"❌ 오류: CSV 로드 중 알 수 없는 오류 발생: {e}")
        return

    required_cols = ['게시물 이름', '게시일', '게시자', '주제']
    if not all(col in df.columns for col in required_cols):
        print(f"❌ 오류: CSV 파일에 필요한 컬럼({', '.join(required_cols)}) 중 일부가 누락되었습니다. 컬럼 이름을 확인해 주세요.")
        return

    # 각 행을 순회하며 포스트 생성
    df.apply(create_jekyll_post, axis=1)

if __name__ == "__main__":
    main()