"""from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

# 브라우저 열기
browser = webdriver.Chrome()

# 네이버 예약 시스템 접속
browser.get('https://booking.naver.com/')

# 로그인 정보 입력
browser.find_element_by_name('id').send_keys('아이디')
browser.find_element_by_name('pw').send_keys('비밀번호')
browser.find_element_by_css_selector('input.btn_login').click()

# 예약 페이지로 이동
browser.find_element_by_css_selector('a.gnb_nav04').click()
browser.find_element_by_css_selector('a[href="/booking/booking_list.nhn"]').click()
browser.find_element_by_css_selector('a[href="/booking/booking_item.nhn"]').click()

# 예약 정보 입력
browser.find_element_by_css_selector('a.btn_select_calendar').click()
browser.find_element_by_css_selector('td.date.on > a').click()
browser.find_element_by_css_selector('button.btn_candi_search').click()

# 최종 예약
browser.find_element_by_css_selector('li.item_item a.item_title').click()
browser.find_element_by_css_selector('button.btn_reserve').click() 
#
"""