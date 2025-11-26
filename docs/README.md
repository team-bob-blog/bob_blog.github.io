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
  /* Page specific styles */
  .docs-container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 20px 0;
  }

  .page-header {
    text-align: center;
    margin-bottom: 60px;
    padding-bottom: 30px;
    border-bottom: 1px solid #eaeaea;
  }

  .page-header h1 {
    font-size: 2.5rem;
    font-weight: 700;
    color: #1a1a1a;
    margin-bottom: 10px;
  }

  .page-header p {
    font-size: 1.1rem;
    color: #666;
    margin: 0;
  }

  .author-wrapper {
    margin-bottom: 80px;
  }

  .author-profile {
    display: flex;
    align-items: center;
    margin-bottom: 25px;
    padding-left: 10px;
  }

  .author-avatar {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    object-fit: cover;
    margin-right: 18px;
    border: 2px solid #fff;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    background-color: #f0f0f0;
  }

  .author-details {
    display: flex;
    flex-direction: column;
  }

  .author-name {
    font-size: 1.5rem;
    font-weight: 700;
    color: #2d3436;
    margin: 0;
    line-height: 1.2;
  }

  .author-meta {
    font-size: 0.9rem;
    color: #636e72;
    margin-top: 4px;
  }

  .post-count-badge {
    background-color: #eef2f7;
    color: #4a90e2;
    padding: 2px 8px;
    border-radius: 12px;
    font-weight: 600;
    font-size: 0.8rem;
    margin-left: 8px;
    vertical-align: middle;
  }

  .no-posts {
    grid-column: 1 / -1;
    padding: 30px;
    text-align: center;
    background: #f9f9f9;
    border-radius: 12px;
    color: #999;
    font-style: italic;
  }

  @media (max-width: 768px) {
    .page-header h1 { font-size: 2rem; }
    .author-profile { flex-direction: column; align-items: flex-start; }
    .author-avatar { margin-bottom: 10px; }
  }
</style>

<div class="docs-container">
  <div class="page-header">
    <h1>Individual Posts</h1>
    <p>팀원들이 작성한 지식과 경험을 공유합니다.</p>
  </div>

  {% assign team_members = site.data.authors %}
  {% assign posts_limit = 10 %}

  {% for author_entry in team_members %}
    {% assign author_shortname = author_entry[0] %}
    {% assign author_info = author_entry[1] %}
    {% assign author_korean_name = author_info.name %}
    
    {% if author_korean_name %}
      {% assign posts_by_author = site.posts | where: "author", author_shortname | sort: 'date' | reverse %}
      {% assign total_posts = posts_by_author.size %}
      
      <div class="author-wrapper">
        <div class="author-profile">
          <img src="{{ '/assets/img/profile/' | append: author_korean_name | append: '.png' | relative_url }}" 
               alt="{{ author_korean_name }}" 
               class="author-avatar"
               onerror="this.src='{{ '/assets/img/profile/default.png' | relative_url }}'; this.onerror=null;">
          <div class="author-details">
            <h2 class="author-name">
              {{ author_korean_name }}
              <span class="post-count-badge">{{ total_posts }}</span>
            </h2>
            <div class="author-meta">
               Latest posts
            </div>
          </div>
        </div>

        <div class="post-card-grid">
          {% if total_posts == 0 %}
            <div class="no-posts">
              아직 작성된 게시물이 없습니다.
            </div>
          {% else %}
            {% for post in posts_by_author limit: posts_limit %}
              <a href="{{ post.url | relative_url }}" class="modern-post-card">
                <h3 class="modern-post-card-title">{{ post.title }}</h3>
                <div class="modern-post-card-meta">
                  <span class="modern-post-date">{{ post.date | date: "%Y.%m.%d" }}</span>
                  {% if post.categories.size > 0 %}
                    {% assign first_category = post.categories | first %}
                    {% if first_category == "example" and post.categories.size > 1 %}
                        {% assign first_category = post.categories[1] %}
                    {% endif %}
                    <span class="modern-post-category">{{ first_category }}</span>
                  {% endif %}
                </div>
              </a>
            {% endfor %}
          {% endif %}
        </div>
      </div>
    {% endif %}
  {% endfor %}
</div>