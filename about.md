---
layout: page
title: Team - 우리 팀 소개
description: >
  함께 git blog를 운영하는 팀원들을 소개합니다.
hide_description: true
sitemap: false
---

<style>
/* About Page Specific Styles */
.about-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px 0;
}

.team-intro-section {
  text-align: center;
  margin-bottom: 60px;
  padding: 60px 20px;
  background: linear-gradient(to right, #000000, #EB5757); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */ 
  border-radius: 20px;
  color: white;
  /* 수정됨: 배경의 포인트 컬러(#EB5757)를 rgba(235, 87, 87, 0.4)로 변환하여 적용 */
  box-shadow: 0 10px 30px rgba(235, 87, 87, 0.4);
  position: relative;
  overflow: hidden;
}

.team-intro-section::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
  animation: rotate 20s linear infinite;
}

@keyframes rotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.team-intro-content {
  position: relative;
  z-index: 1;
}

.team-intro-section h2 {
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 20px;
  color: white !important;
  text-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.team-intro-section p {
  font-size: 1.1rem;
  line-height: 1.8;
  opacity: 0.95;
  margin: 0 auto;
  max-width: 600px;
}

.member-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 30px;
  margin-top: 40px;
}

.member-card {
  background: #fff;
  border-radius: 20px;
  padding: 40px 30px;
  text-align: center;
  box-shadow: 0 10px 40px rgba(0,0,0,0.05);
  border: 1px solid rgba(0,0,0,0.02);
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.member-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 50px rgba(0,0,0,0.1);
}

.member-card::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 6px;
  background: linear-gradient(90deg, #667eea, #764ba2);
  opacity: 0;
  transition: opacity 0.3s;
}

.member-card:hover::after {
  opacity: 1;
}

.member-img-wrapper {
  width: 140px;
  height: 140px;
  margin-bottom: 25px;
  position: relative;
}

.member-card img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid #fff;
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
  transition: transform 0.3s;
}

.member-card:hover img {
  transform: scale(1.05);
}

.member-card h3 {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0 0 15px 0;
  color: #2d3436;
}

.member-card .goal {
  font-size: 0.95rem;
  color: #636e72;
  line-height: 1.6;
  margin-bottom: 25px;
  flex-grow: 1;
}

.member-card .blog-link {
  display: inline-flex;
  align-items: center;
  padding: 10px 24px;
  background: #f1f3f5;
  color: #495057 !important;
  border-radius: 50px;
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 600;
  transition: all 0.2s;
}

.member-card .blog-link:hover {
  background: #4a90e2;
  color: white !important;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(74, 144, 226, 0.3);
}

@media (max-width: 768px) {
  .team-intro-section h2 { font-size: 2rem; }
  .member-grid { grid-template-columns: 1fr; }
}
</style>

<div class="about-container">

<div class="team-intro-section">
  <div class="team-intro-content">
    <h2>🚀 구미 3반 블로그 스터디</h2>
    <p>
      우리는 함께 성장하는 개발자들입니다.<br>
      개인적인 CS 공부를 정리하고, 서로의 지식을 공유하며<br>
      더 나은 내일을 만들어갑니다.
    </p>
  </div>
</div>

<div class="member-grid">

<div class="member-card">
  <div class="member-img-wrapper">
    <img src="{{ '/assets/img/profile/김강연.png' | relative_url }}" alt="김강연" onerror="this.src='{{ '/assets/img/profile/default.png' | relative_url }}'">
  </div>
  <h3>김강연</h3>
  <p class="goal">"꾸준함이 재능을 이긴다"<br>파이썬 심화 학습 및 백엔드 기술 정복</p>
  <a href="https://derek0517.tistory.com/" target="_blank" class="blog-link">블로그 방문</a>
</div>

<div class="member-card">
  <div class="member-img-wrapper">
    <img src="{{ '/assets/img/profile/장진욱.png' | relative_url }}" alt="장진욱" onerror="this.src='{{ '/assets/img/profile/default.png' | relative_url }}'">
  </div>
  <h3>장진욱</h3>
  <p class="goal">"CS On CS"<br>컴퓨터 구조와 운영체제의 깊이를 더하다</p>
  <a href="https://jjw3300.tistory.com/" target="_blank" class="blog-link">블로그 방문</a>
</div>

<div class="member-card">
  <div class="member-img-wrapper">
    <img src="{{ '/assets/img/profile/정수민.png' | relative_url }}" alt="정수민" onerror="this.src='{{ '/assets/img/profile/default.png' | relative_url }}'">
  </div>
  <h3>정수민</h3>
  <p class="goal">"Always Number One"<br>알고리즘 마스터를 향한 여정</p>
  <a href="https://ss-coding-99.tistory.com/" target="_blank" class="blog-link">블로그 방문</a>
</div>

<div class="member-card">
  <div class="member-img-wrapper">
    <img src="{{ '/assets/img/profile/배재유.png' | relative_url }}" alt="배재유" onerror="this.src='{{ '/assets/img/profile/default.png' | relative_url }}'">
  </div>
  <h3>배재유</h3>
  <p class="goal">"기록은 기억을 지배한다"<br>Java와 시스템 프로그래밍의 모든 것</p>
  <a href="https://platypus3036.tistory.com/" target="_blank" class="blog-link">블로그 방문</a>
</div>

<div class="member-card">
  <div class="member-img-wrapper">
    <img src="{{ '/assets/img/profile/김민재.png' | relative_url }}" alt="김민재" onerror="this.src='{{ '/assets/img/profile/default.png' | relative_url }}'">
  </div>
  <h3>김민재</h3>
  <p class="goal">"학습의 관성"<br>스스로 학습하고 정리하는 습관 만들기</p>
  <a href="https://blopz.tistory.com/" target="_blank" class="blog-link">블로그 방문</a>
</div>

</div>
</div>