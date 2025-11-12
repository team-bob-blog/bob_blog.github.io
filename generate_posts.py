import pandas as pd
from datetime import datetime
import os
import re

# ==============================================================================
# 설정: CSV 파일 경로, 폴더, 날짜 형식, 작성자별 색상 매핑
# ==============================================================================
CSV_FILE_PATH = 'blog.csv' 
POSTS_DIR = 'example/_posts'
DATE_FORMAT_IN_CSV = r'(\d{4})년 (\d{1,2})월 (\d{1,2})일'

BASE_URL_FORMAT = "/{}/{}/{}/{}/" 

# Hydejack authors.yml의 영문 shortname과 연결하기 위한 매핑
AUTHOR_SHORTNAMES = {
    '김강연': 'kimkangyeon',
    '장진욱': 'jangjinwook',
    '정수민': 'jungsumin',
    '배재유': 'baejaeyu',
    '김민재': 'kimminjae'
}
# _data/author_colors.yml 생성을 위한 색상 정보
AUTHOR_COLORS = {
    '김강연': '#007bff',
    '장진욱': '#28a745',
    '정수민': '#6f42c1',
    '배재유': '#001f3f',
    '김민재': '#fd7e14'
}
# DATA_DIR 정의 (os.path.abspath 대신 상대 경로 사용)
DATA_DIR = os.path.join(os.getcwd(), 'example/_data')

# ==============================================================================
# 함수 정의
# ==============================================================================

def create_jekyll_post(row):
    """CSV 한 행의 데이터를 Jekyll 포스트 파일로 생성하고 <iframe> 구조를 추가합니다."""
    
    # 1. 데이터 파싱 (KeyError 발생 시 즉시 오류 보고)
    post_title = str(row['게시물 이름']).strip()
    author_korean = str(row['게시자']).strip()
    topics = str(row['주제']).strip()
    
    post_url_str = str(row.get('URL 게시', '')).strip() 
    
    author_shortname = AUTHOR_SHORTNAMES.get(author_korean, 'default_author')
    external_link = post_url_str if post_url_str.startswith(('http://', 'https://')) else ''
    
    if not post_title:
        print(f"⚠️ 경고: 게시물 이름이 비어있어 해당 행을 스킵합니다.")
        return

    date_match = re.search(DATE_FORMAT_IN_CSV, str(row['게시일']))
    if not date_match:
        print(f"⚠️ 경고: '{post_title}' 게시물의 날짜 형식을 인식할 수 없습니다. 스킵합니다.")
        return

    year, month, day = date_match.groups()
    post_date = datetime(int(year), int(month), int(day))
    last_modified = post_date.strftime('%Y-%m-%d')

    # 2. 파일명 및 링크 생성 (파일명 안전화 적용)
    slug = re.sub(r'[^\w\s-]', '', post_title).strip().replace(' ', '-').lower()
    filename_slug = slug 
    filename = f"{post_date.strftime('%Y-%m-%d')}-{filename_slug}.md"
    
    filepath = os.path.join(POSTS_DIR, filename)

    # 3. Front Matter (YAML 헤더) 생성
    tags_list = [t.strip() for t in topics.split(',') if t.strip()]
    category = tags_list[0] if tags_list else '미분류'
    tags_yaml = '[' + ', '.join([f"'{t}'" for t in tags_list]) + ']'

    front_matter = f"""---
layout: post
title: "{post_title}"
author: {author_shortname} 
date: {post_date.strftime('%Y-%m-%d 00:00:00 +0900')}
last_modified_at: {last_modified}
categories: [{category}]
tags: {tags_yaml}
excerpt_separator: "---"
---
"""
    
    # 4. Markdown 본문 내용 추가 
    
    # 목록 페이지(Excerpt)에 표시될 요약 텍스트 (블로그 목록에 표시됨)
    summary_text = f"**[{author_korean}]** {post_title} 주제에 대한 게시글입니다. [자세히 보기...]"
    
    # <iframe> 생성 (상세 페이지에 표시됨)
    iframe_html = ""
    if external_link:
        iframe_html = f"""<iframe src="{external_link}" 
        width="100%" 
        height="800px" 
        frameborder="0">
</iframe>"""
    
    # Liquid Toggle (작성자 정보 토글 - 상세 페이지에 표시됨)
    liquid_toggle_final = """{%- include author_info_toggle.html author=page.author -%}"""
    
    # 최종 본문 구성: 요약 -> --- (구분선) -> <iframe> -> Liquid Toggle
    post_content = f"""{summary_text}

---

{iframe_html}

{liquid_toggle_final}
"""
    
    final_content = front_matter + post_content

    # 5. 파일 저장
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_content.strip()) 
        print(f"✅ 파일 생성 완료: {filepath}")
    except Exception as e:
        print(f"❌ 파일 생성 실패 ({filepath}): {e}")


def main():
    """메인 함수: CSV를 로드하고 포스트 생성을 시작하며, _data 파일도 생성합니다."""
    
    os.makedirs(POSTS_DIR, exist_ok=True)
    os.makedirs(DATA_DIR, exist_ok=True) 

    # _data/author_colors.yml 파일 생성
    try:
        yaml_content = ""
        for k, v in AUTHOR_COLORS.items():
            yaml_content += f"{k}: '{v}'\n"
        
        with open(os.path.join(DATA_DIR, 'author_colors.yml'), 'w', encoding='utf-8') as f:
            f.write(yaml_content)
    except Exception as e:
        print(f"❌ 설정 파일 생성 실패: {e}")


    required_cols = ['게시물 이름', '게시일', '게시자', '주제', 'URL 게시']
    
    df = None
    encodings = ['utf-8', 'euc-kr', 'cp949']
    
    for encoding in encodings:
        try:
            # Python의 csv.Sniffer를 이용한 자동 구분자 감지
            with open(CSV_FILE_PATH, 'r', encoding=encoding) as f:
                first_line = f.readline()
                # 콤마가 있으면 콤마, 없으면 탭으로 추정
                if ',' in first_line:
                    delimiter = ','
                elif '\t' in first_line:
                    delimiter = '\t'
                else:
                    delimiter = ','
            
            df = pd.read_csv(CSV_FILE_PATH, encoding=encoding, delimiter=delimiter)
            print(f"✅ CSV 로드 성공: 인코딩={encoding}, 구분자={repr(delimiter)}")
            break
        except Exception as e:
            continue
    
    if df is None:
        print(f"❌ 오류: CSV 로드 중 치명적인 오류 발생")
        return

    # --- [컬럼 확인 및 처리] ---
    if df is not None:
        # 1. 컬럼 이름의 앞뒤 공백을 제거하여 비교합니다.
        df.columns = df.columns.str.strip()
        
        # 2. 필수 컬럼이 모두 존재하는지 확인
        if not all(col in df.columns for col in required_cols):
            missing_cols = [col for col in required_cols if col not in df.columns]
            
            print(f"❌ 오류: CSV 파일에 필요한 컬럼({', '.join(required_cols)}) 중 일부({', '.join(missing_cols)})가 누락되었습니다.")
            print(f"✅ CSV 파일에서 실제로 읽은 컬럼 목록: {df.columns.tolist()}")
            print("💡 CSV 파일의 헤더를 확인하여 대소문자, 공백, 델리미터 분리를 정확히 일치시켜 주세요.")
            return

        # 각 행을 순회하며 포스트 생성
        df.apply(create_jekyll_post, axis=1)
    
if __name__ == "__main__":
    main()