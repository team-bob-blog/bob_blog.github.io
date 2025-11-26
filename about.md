---
layout: page
title: Team - 우리 팀 소개
description: >
  함께 git blog를 운영하는 팀원들을 소개합니다.
hide_description: true
sitemap: false
---

<style>
.team-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
}

.team-intro {
  text-align: center;
  margin-bottom: 40px;
  padding: 30px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 16px;
  color: white;
}

.team-intro h2 {
  font-size: 1.8rem;
  margin-bottom: 15px;
  color: white !important;
}

.team-intro p {
  font-size: 1rem;
  line-height: 1.8;
  opacity: 0.95;
  margin: 0;
}

.member-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 25px;
  margin-top: 30px;
}

.member-card {
  background: #fff;
  border-radius: 16px;
  padding: 30px 25px;
  text-align: center;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
  border: 1px solid #f0f0f0;
  transition: transform 0.3s, box-shadow 0.3s;
}

.member-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 30px rgba(0,0,0,0.12);
}

.member-card img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 20px;
  border: 4px solid #f0f0f0;
}

.member-card h3 {
  font-size: 1.3rem;
  margin: 0 0 10px 0;
  color: #333;
}

.member-card .goal {
  font-size: 0.9rem;
  color: #666;
  line-height: 1.6;
  margin-bottom: 15px;
  min-height: 50px;
}

.member-card .blog-link {
  display: inline-block;
  padding: 8px 20px;
  background: #4a90e2;
  color: white !important;
  border-radius: 20px;
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 600;
  transition: background 0.2s;
}

.member-card .blog-link:hover {
  background: #357abd;
  text-decoration: none;
}

@media (max-width: 600px) {
  .member-grid {
    grid-template-columns: 1fr;
  }
  .team-intro h2 {
    font-size: 1.4rem;
  }
}
</style>

<div class="team-container">

<div class="team-intro">
  <h2>🚀 구미 3반 블로그 스터디</h2>
  <p>
    개인적인 CS 공부를 블로그를 통해 정리하고<br>
    스터디 구성원에게 지식을 공유하는 스터디입니다.
  </p>
</div>

<div class="member-grid">

<div class="member-card">
  <img src="{{ '/assets/img/profile/김강연.png' | relative_url }}" alt="김강연">
  <h3>김강연</h3>
  <p class="goal">파이썬 심화 학습 및 백엔드 기술 공부<br>블로그 작성 습관 만들기</p>
  <a href="https://derek0517.tistory.com/" target="_blank" class="blog-link">블로그 방문</a>
</div>

<div class="member-card">
  <img src="{{ '/assets/img/profile/장진욱.png' | relative_url }}" alt="장진욱">
  <h3>장진욱</h3>
  <p class="goal">알고리즘 스터디 당일 바로 작성<br>주 1회 이상 자유 주제 작성</p>
  <a href="https://jjw3300.tistory.com/" target="_blank" class="blog-link">블로그 방문</a>
</div>

<div class="member-card">
  <img src="{{ '/assets/img/profile/정수민.png' | relative_url }}" alt="정수민">
  <h3>정수민</h3>
  <p class="goal">항상 1등한다는 마인드</p>
  <a href="https://ss-coding-99.tistory.com/" target="_blank" class="blog-link">블로그 방문</a>
</div>

<div class="member-card">
  <img src="{{ '/assets/img/profile/배재유.png' | relative_url }}" alt="배재유">
  <h3>배재유</h3>
  <p class="goal">개발자의 꿈은 기록하다<br>습관으로 만들자</p>
  <a href="https://platypus3036.tistory.com/" target="_blank" class="blog-link">블로그 방문</a>
</div>

<div class="member-card">
  <img src="{{ '/assets/img/profile/김민재.png' | relative_url }}" alt="김민재">
  <h3>김민재</h3>
  <p class="goal">스스로 학습하고 정리하는 관성 만들기</p>
  <a href="https://blopz.tistory.com/" target="_blank" class="blog-link">블로그 방문</a>
</div>

</div>
</div>