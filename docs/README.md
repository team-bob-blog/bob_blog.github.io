---
layout: page
title: 개인별 게시물 목록
description: >
    팀원별 게시물 목록을 확인하고 해당 글로 이동할 수 있습니다. (10개씩 분리)
hide_description: true
sitemap: false
permalink: /docs/
---
<style>
/* ... (스타일 코드는 이전과 동일하게 유지) ... */
.author-section {
    margin-bottom: 40px;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    background: #ffffff;
}

.author-header {
    background: #4a90e2;
    color: white;
    padding: 15px 25px;
}

.author-header h2 {
    margin: 0;
    color: white;
    font-size: 1.6rem;
    font-weight: 500;
}

.posts-container {
    padding: 0 20px;
}

.post-item {
    display: flex;
    flex-direction: column;
    padding: 15px 0;
    border-bottom: 1px solid #eeeeee;
}

.post-item:last-child {
    border-bottom: none;
}

.post-item:hover {
    background-color: #f7f7f7;
    cursor: pointer;
}

.post-meta-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 5px;
}

.post-title-link {
    font-size: 1.1rem;
    font-weight: 600;
    color: #2c3e50;
    text-decoration: none;
    margin-bottom: 5px;
}

.post-title-link:hover {
    color: #4a90e2;
    text-decoration: underline;
}

.post-category {
    display: inline-block;
    padding: 4px 10px;
    background: #e6f7ff;
    color: #1890ff;
    border-radius: 4px;
    font-size: 0.8em;
    font-weight: 500;
    margin-right: 8px;
}

.post-date {
    color: #95a5a6;
    white-space: nowrap;
    font-size: 0.85em;
}

.post-tags {
    color: #95a5a6;
    font-size: 0.85em;
    margin-left: 10px;
}
/* 페이지네이션 관련 스타일 제거 */
/* .pagination-links {
    text-align: center;
    padding: 15px 0;
    border-top: 1px solid #eee;
    margin-top: 10px;
}

.pagination-links a, .pagination-links span {
    padding: 8px 12px;
    margin: 0 4px;
    text-decoration: none;
    border-radius: 4px;
    font-size: 0.9em;
    font-weight: 600;
}

.pagination-links a {
    background: #e6f7ff;
    color: #4a90e2;
}

.pagination-links span {
    background: #4a90e2;
    color: white;
} */

</style>

# 🧑‍💻 개인별 게시물 문서 메인

<p style="color: #666; margin-bottom: 30px;">
이 페이지는 팀원별로 작성된 포스트 목록을 제공합니다. (페이지당 10개)
</p>

{% assign team_members = site.data.authors %}

{% comment %} 
페이지네이션을 위해 URL에서 쿼리 파라미터를 가져와 분리합니다. 
각 작가별로 'page_작가shortname' 형태의 파라미터를 기대합니다.
{% endcomment %}

{% assign posts_per_page = 10 %}

{% for author_entry in team_members %}
    {% assign author_shortname = author_entry[0] %}
    {% assign author_info = author_entry[1] %}
    {% assign author_korean_name = author_info.name %}

    {% comment %} 
    쿼리 파라미터에서 현재 작가의 페이지 번호를 찾습니다.
    예시: /docs/?page_kimkangyeon=2
    Liquid는 직접 쿼리 파싱이 불가능하므로, 기본적으로 1로 설정합니다.
    {% endcomment %}
    
    {% assign current_author_page = 1 %}
    
    {% comment %} 이 부분은 서버 빌드 환경의 제약으로 인해 Liquid만으로 동적 쿼리 파싱은 불가능하며, 
    모든 작가에게 page=1로 기본값이 적용됩니다. 실제 페이지 이동은 링크를 수동 클릭해야 합니다. {% endcomment %}

    {% if author_korean_name %}
      
<div class="author-section">
    <div class="author-header">
        <h2>{{ author_korean_name }}</h2>
    </div>

{% assign posts_by_author = site.posts | where: "author", author_shortname | sort: 'date' | reverse %}
{% assign total_posts = posts_by_author.size %}

{% assign total_pages = total_posts | divided_by: posts_per_page %}
{% assign remainder = total_posts | modulo: posts_per_page %}
{% if remainder > 0 %}{% assign total_pages = total_pages | plus: 1 %}{% endif %}

{% assign offset = current_author_page | minus: 1 | times: posts_per_page %}
{% assign paginated_posts = posts_by_author | limit: posts_per_page | offset: offset %}


    <div class="posts-container">

{% if total_posts == 0 %}
    <div class="no-posts" style="padding: 20px; color: #95a5a6;">
        작성된 게시물이 없습니다.
    </div>
{% else %}

    {% comment %} 포스트 목록 출력 {% endcomment %}
    {% for post in paginated_posts %}
      
        <div class="post-item" onclick="window.location.href='{{ post.url | relative_url }}'">
            <a href="{{ post.url | relative_url }}" class="post-title-link">
                {{ post.title }}
            </a>
            <div class="post-meta-row">
                <div>
                    {% for category in post.categories %}
                        {% unless category == "example" %}
                            <span class="post-category">{{ category }}</span>
                        {% endunless %}
                    {% endfor %}
                    <span class="post-tags">#{{ post.tags | join: ' #' }}</span>
                </div>
                <div class="post-date">{{ post.date | date: "%Y년 %m월 %d일" }}</div>
            </div>
        </div>
        
    {% endfor %}
    
    </div>
    
    {% comment %} 수동 페이지네이션 링크 생성 코드를 제거했습니다. {% endcomment %}
    

{% endif %}
</div>
    
    {% endif %}
{% endfor %}