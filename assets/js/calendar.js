// 캘린더 전역 변수
var calendarData = [];
var calendarPostsMap = {};
var calendarCurrDate = new Date();

var calendarAuthorColors = {
  'jungsumin':   { name: '정수민', color: '#339af0' },
  'kimkangyeon': { name: '김강연', color: '#ff6b6b' },
  'jangjinwook': { name: '장진욱', color: '#51cf66' },
  'baejaeyu':    { name: '배재유', color: '#8d6e63' },
  'kimminjae':   { name: '김민재', color: '#cc5de8' },
  'default':     { name: '멤버',   color: '#adb5bd' }
};

function getCalendarAuthorStyle(id) {
  return calendarAuthorColors[id] || calendarAuthorColors['default'];
}

function initCalendarData() {
  try {
    var dataEl = document.getElementById('calendar-data');
    if (dataEl) {
      var rawText = dataEl.textContent.trim();
      console.log('Calendar: Raw data length:', rawText.length);
      calendarData = JSON.parse(rawText);
      console.log('Calendar: Parsed posts:', calendarData.length);
      calendarPostsMap = {};
      calendarData.forEach(function(p) {
        if (!calendarPostsMap[p.date]) calendarPostsMap[p.date] = [];
        calendarPostsMap[p.date].push(p);
      });
    }
  } catch(e) {
    console.error("Calendar data parse error:", e);
  }
}

function renderCalendar() {
  var monthDisplay = document.getElementById('monthDisplay');
  var postCountInfo = document.getElementById('postCountInfo');
  var grid = document.getElementById('calendarGrid');

  if (!grid) return;

  var year = calendarCurrDate.getFullYear();
  var month = calendarCurrDate.getMonth();
  var todayStr = new Date().toISOString().split('T')[0];

  if (monthDisplay) monthDisplay.innerText = year + '년 ' + (month + 1) + '월';

  var count = 0;
  var monthPrefix = year + '-' + String(month + 1).padStart(2, '0');
  Object.keys(calendarPostsMap).forEach(function(date) {
    if (date.indexOf(monthPrefix) === 0) {
      count += calendarPostsMap[date].length;
    }
  });
  if (postCountInfo) postCountInfo.innerText = '총 ' + count + '개의 포스팅';

  grid.innerHTML = '';

  var firstDay = new Date(year, month, 1).getDay();
  var lastDate = new Date(year, month + 1, 0).getDate();

  for (var i = 0; i < firstDay; i++) {
    var emptyCell = document.createElement('div');
    emptyCell.className = 'day-cell other-month';
    grid.appendChild(emptyCell);
  }

  for (var d = 1; d <= lastDate; d++) {
    var dateKey = year + '-' + String(month + 1).padStart(2, '0') + '-' + String(d).padStart(2, '0');
    var dayPosts = calendarPostsMap[dateKey] || [];
    var isToday = dateKey === todayStr ? ' today' : '';

    var cell = document.createElement('div');
    cell.className = 'day-cell' + isToday;
    cell.setAttribute('data-date', dateKey);
    cell.setAttribute('onclick', 'selectCalendarDate("' + dateKey + '", this)');

    var dotsHtml = '';
    if (dayPosts.length > 0) {
      dotsHtml = '<div class="dots-container">';
      var showCount = Math.min(dayPosts.length, 6);
      for (var j = 0; j < showCount; j++) {
        var style = getCalendarAuthorStyle(dayPosts[j].author);
        dotsHtml += '<div class="dot" style="background-color:' + style.color + ';"></div>';
      }
      if (dayPosts.length > 6) {
        dotsHtml += '<span class="more-badge">+' + (dayPosts.length - 6) + '</span>';
      }
      dotsHtml += '</div>';
    }

    cell.innerHTML = '<span class="day-number">' + d + '</span>' + dotsHtml;
    grid.appendChild(cell);
  }
}

function selectCalendarDate(date, element) {
  var grid = document.getElementById('calendarGrid');
  var scheduleList = document.getElementById('scheduleList');
  var dateTitle = document.getElementById('selectedDateTitle');

  if (grid) {
    var cells = grid.querySelectorAll('.day-cell');
    for (var i = 0; i < cells.length; i++) {
      cells[i].classList.remove('selected');
    }
  }
  if (element) element.classList.add('selected');

  var parts = date.split('-');
  if (dateTitle) dateTitle.innerText = parts[0] + '년 ' + parts[1] + '월 ' + parts[2] + '일 스케줄';

  var dayPosts = calendarPostsMap[date] || [];

  if (!scheduleList) return;

  if (dayPosts.length === 0) {
    scheduleList.innerHTML = '<div class="empty-message">작성된 게시물이 없습니다. 😴</div>';
  } else {
    var html = '';
    dayPosts.forEach(function(post) {
      var style = getCalendarAuthorStyle(post.author);
      html += '<a href="' + post.url + '" class="schedule-item">' +
        '<span class="author-badge" style="background-color:' + style.color + ';">' + style.name + '</span>' +
        '<span class="post-title">' + post.title + '</span></a>';
    });
    scheduleList.innerHTML = html;
  }
}

function calendarPrevMonth() {
  calendarCurrDate.setMonth(calendarCurrDate.getMonth() - 1);
  renderCalendar();
}

function calendarNextMonth() {
  calendarCurrDate.setMonth(calendarCurrDate.getMonth() + 1);
  renderCalendar();
}

function calendarGoToday() {
  calendarCurrDate = new Date();
  renderCalendar();
}

function initCalendar() {
  console.log('Calendar: init called');
  initCalendarData();
  renderCalendar();
}

// 전역으로 노출
window.initCalendar = initCalendar;
window.calendarPrevMonth = calendarPrevMonth;
window.calendarNextMonth = calendarNextMonth;
window.calendarGoToday = calendarGoToday;
window.selectCalendarDate = selectCalendarDate;

// 자동 실행: calendar-data 요소가 있으면 바로 초기화
(function autoInit() {
  function tryInit() {
    var dataEl = document.getElementById('calendar-data');
    if (dataEl) {
      console.log('Calendar: Auto-init triggered');
      initCalendar();
    }
  }
  
  // DOM 상태에 따라 실행
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', tryInit);
  } else {
    tryInit();
  }
  
  // Hydejack push-state 지원 - 여러 이벤트에 등록
  var pushStateEl = document.getElementById('_pushState');
  if (pushStateEl) {
    pushStateEl.addEventListener('hy-push-state-load', function() {
      setTimeout(tryInit, 50);
    });
    pushStateEl.addEventListener('hy-push-state-after', function() {
      setTimeout(tryInit, 50);
    });
  }
  
  // window 이벤트로도 등록 (백업)
  window.addEventListener('hy-push-state-after', function() {
    setTimeout(tryInit, 50);
  });
})();
