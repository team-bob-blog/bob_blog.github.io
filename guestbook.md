---
layout: page
title: 방명록
description: 방문해 주셔서 감사합니다!
permalink: /guestbook/
---

<div class="guestbook-header">
  <div class="guestbook-icon">📝</div>
  <h2>환영합니다!</h2>
  <p class="guestbook-description">
    방문하신 모든분들께 감사드리며!<br>
    블로그 스터디의 피드백 환영합니다!!
  </p>
  <p class="guestbook-contact">
    📧 블로그 스터디에 대한 문의는 <a href="mailto:dmdm0601@naver.com">dmdm0601@naver.com</a>으로 연락바랍니다!
  </p>
</div>

<div class="guestbook-form-section">
  <h3>✍️ 방명록 남기기</h3>
  <p class="guestbook-note">GitHub 계정으로 로그인하여 방명록을 남겨주세요!</p>
</div>

<script src="https://utteranc.es/client.js"
        repo="team-bob-blog/bob_blog.github.io"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>

<style>
.guestbook-header {
  text-align: center;
  padding: 40px 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 16px;
  color: white;
  margin-bottom: 30px;
}

.guestbook-icon {
  font-size: 4rem;
  margin-bottom: 10px;
}

.guestbook-header h2 {
  margin: 0 0 15px 0;
  font-size: 2rem;
}

.guestbook-description {
  font-size: 1.1rem;
  line-height: 1.8;
  opacity: 0.95;
  margin-bottom: 20px;
}

.guestbook-contact {
  background: rgba(255,255,255,0.2);
  padding: 15px 25px;
  border-radius: 10px;
  display: inline-block;
}

.guestbook-contact a {
  color: #fff;
  font-weight: bold;
  text-decoration: underline;
}

.guestbook-form-section {
  background: #f8f9fa;
  padding: 25px;
  border-radius: 12px;
  margin-bottom: 20px;
  text-align: center;
}

.guestbook-form-section h3 {
  margin: 0 0 10px 0;
  color: #2d3436;
}

.guestbook-note {
  color: #636e72;
  font-size: 0.95rem;
  margin: 0;
}

.utterances {
  max-width: 100% !important;
}
</style>
