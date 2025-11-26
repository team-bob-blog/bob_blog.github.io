---
layout: page
title: 개인별 게시물 목록
description: >
    팀원별 게시물 목록을 확인하고 해당 글로 이동할 수 있습니다.
hide_description: true
sitemap: false
permalink: /docs/
---

<style>
.docs-container {
  max-width: 900px;
  margin: 0 auto;
}

.docs-header {
  text-align: center;
  padding: 30px 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 16px;
  margin-bottom: 30px;
  color: white;
}

.docs-header h1 {
  font-size: 1.6rem;
  margin: 0 0 10px 0;
  color: white !important;
}

.docs-header p {
  margin: 0;
  opacity: 0.9;
  font-size: 0.95rem;
}

.author-section {
  margin-bottom: 25px;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
  background: #ffffff;
  border: 1px solid #f0f0f0;
}

.author-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px;
  cursor: pointer;
  transition: background 0.2s;
  border-bottom: 1px solid #f0f0f0;
}

.author-header:hover {
  background: #fafafa;
}

.author-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.author-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 1rem;
}

.author-name {
  font-size: 1.1rem;
  font-weight: 600;
  color: #333;
  margin: 0;
}

.post-count {
  background: #e8f4fd;
  color: #1a73e8;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
}

.posts-container {
  padding: 0;
  max-height: 400px;
  overflow-y: auto;
}

.post-item {
  display: flex;
  align-items: center;
  padding: 14px 20px;
  border-bottom: 1px solid #f5f5f5;
  transition: background 0.2s;
  text-decoration: none !important;
}

.post-item:last-child {
  border-bottom: none;
}

.post-item:hover {
  background: #f8f9fa;
}

.post-date-badge {
  min-width: 50px;
  text-align: center;
  margin-right: 15px;
}

.post-date-badge .day {
  font-size: 1.3rem;
  font-weight: 700;
  color: #333;
  line-height: 1;
}

.post-date-badge .month {
  font-size: 0.7rem;
  color: #888;
  text-transform: uppercase;
}

.post-content {
  flex: 1;
  min-width: 0;
}

.post-title {
  font-size: 0.95rem;
  font-weight: 600;
  color: #333 !important;
  margin: 0 0 4px 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.post-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.post-category {
  display: inline-block;
  padding: 2px 8px;
  background: #e8f4fd;
  color: #1a73e8;
  border-radius: 4px;
  font-size: 0.7rem;
  font-weight: 600;
}

.post-tags {
  color: #999;
  font-size: 0.75rem;
}

.no-posts {
  padding: 30px;
  text-align: center;
  color: #999;
  font-style: italic;
}

.view-more {
  display: block;
  text-align: center;
  padding: 12px;
  background: #f8f9fa;
  color: #666;
  font-size: 0.85rem;
  text-decoration: none;
  border-top: 1px solid #f0f0f0;
}

.view-more:hover {
  background: #f0f0f0;
  color: #333;
}

@media (max-width: 600px) {
  .docs-header h1 { font-size: 1.3rem; }
  .post-date-badge { display: none; }
  .author-header { padding: 12px 15px; }
  .post-item { padding: 12px 15px; }
}
</style>

<div class="docs-container">

<div class="docs-header">
  <h1>📚 팀원별 게시물</h1>
  <p>각 팀원이 작성한 포스트를 한눈에 확인하세요</p>
</div>

{% assign team_members = site.data.authors %}
{% assign posts_per_page = 10 %}

{% for author_entry in team_members %}
  {% assign author_shortname = author_entry[0] %}
  {% assign author_info = author_entry[1] %}
  {% assign author_korean_name = author_info.name %}
  {% assign first_char = author_korean_name | slice: 0 %}

  {% if author_korean_name %}
    {% assign posts_by_author = site.posts | where: "author", author_shortname | sort: 'date' | reverse %}
    {% assign total_posts = posts_by_author.size %}

<div class="author-section">
  <div class="author-header">
    <div class="author-info">
      <div class="author-avatar">{{ first_char }}</div>
      <h3 class="author-name">{{ author_korean_name }}</h3>
    </div>
    <span class="post-count">{{ total_posts }}개</span>
  </div>

  <div class="posts-container">
    {% if total_posts == 0 %}
      <div class="no-posts">아직 작성된 게시물이 없습니다</div>
    {% else %}
      {% for post in posts_by_author limit: posts_per_page %}
        <a href="{{ post.url | relative_url }}" class="post-item">
          <div class="post-date-badge">
            <div class="day">{{ post.date | date: "%d" }}</div>
            <div class="month">{{ post.date | date: "%b" }}</div>
          </div>
          <div class="post-content">
            <div class="post-title">{{ post.title }}</div>
            <div class="post-meta">
              {% for category in post.categories %}
                {% unless category == "example" %}
                  <span class="post-category">{{ category }}</span>
                {% endunless %}
              {% endfor %}
              {% if post.tags.size > 0 %}
                <span class="post-tags">#{{ post.tags | first }}</span>
              {% endif %}
            </div>
          </div>
        </a>
      {% endfor %}
      {% if total_posts > posts_per_page %}
        <a href="{{ '/docs/authors/' | append: author_shortname | append: '/' | relative_url }}" class="view-more">
          + {{ total_posts | minus: posts_per_page }}개 더보기
        </a>
      {% endif %}
    {% endif %}
  </div>
</div>

  {% endif %}
{% endfor %}

</div>