---
layout: page
title: "배재유의 전체 게시물"
author_shortname: baejaeyu
description: >
  배재유 님의 모든 작성 글 목록입니다.
hide_description: true
sitemap: false
permalink: /docs/authors/baejaeyu/
---
<style>
/* (스타일 코드는 공간 절약을 위해 생략하며, 이전에 제공된 모던 UI 스타일을 _includes에 넣어야 합니다.) */
.author-section { 
  margin-bottom: 40px; border-radius: 12px; overflow: hidden; 
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); background: #ffffff;
}
.author-header { background: #4a90e2; color: white; padding: 15px 25px; }
.posts-container { padding: 0 20px; }
.post-item { padding: 15px 0; border-bottom: 1px dashed #eee; cursor: pointer; }
.post-title-link { font-size: 1.1em; font-weight: 600; color: #2c3e50; text-decoration: none; }
.post-meta-row { font-size: 0.9em; color: #95a5a6; margin-top: 5px; }
.post-category { background: #e6f7ff; color: #1890ff; padding: 3px 8px; border-radius: 4px; }
</style>
# 📑 배재유 님의 전체 포스트 목록

{% assign target_author = page.author_shortname %}

{% assign posts_by_author = site.posts | where: "author", target_author | sort: 'date' | reverse %}
{% assign total_posts = posts_by_author.size %}

<div class="posts-container">
{% if total_posts == 0 %}
  <p style="padding: 20px; color: #95a5a6; font-style: italic;">
    아직 작성된 게시물이 없습니다.
  </p>
{% else %}
  <ul style="list-style-type: none; padding-left: 0;">
  {% for post in posts_by_author %}
    
    <li class="post-item" onclick="window.location.href='{{ post.url | relative_url }}'">
      <a href="{{ post.url | relative_url }}" class="post-title-link">
        {{ post.title }}
      </a>
      <div class="post-meta-row">
        {% for category in post.categories %}
          {% unless category == "example" %}
            <span class="post-category">{{ category }}</span>
          {% endunless %}
        {% endfor %}
        <span class="post-tags">#{{ post.tags | join: ' #' }}</span>
        <span class="post-date" style="margin-left: 15px;">{{ post.date | date: "%Y년 %m월 %d일" }}</span>
      </div>
    </li>
      
  {% endfor %}
  </ul>
  
  <p style="margin-top: 20px; padding-bottom: 10px;">총 **{{ total_posts }}** 개의 게시물이 있습니다.</p>

{% endif %}
</div>