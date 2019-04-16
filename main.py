from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.chrome.options import Options
import sites
import mongo, gmail
import sys

# 크롬드라이버의 추가 옵션을 설정하는 함수
options = Options()

# chrome 에서 F11을 눌러 전체 화면으로 넓히는 옵션 --kiosk , --start-fullscreen
options.add_argument('--kiosk')
# options.add_argument('headless')    # 창이 안보이게 돌리기

# 2일전 기준날짜 (월요일은 주말 포함 3일)
date = datetime.today().weekday()
if date:
    standard_date = datetime.today() - timedelta(2)
else:
    # 0이면 월요일, false 이므로, 주말포함 3일전공고
    standard_date = datetime.today() - timedelta(3)

# 13개 사이트 16개 정보저장

sys.stdout = open('result.txt', 'w')

''' 
kotra, nipa, sba, kisa, nia, kdata, moel, bepa
'''
# 코트라
sites.kotra_scan()

# 정보통신산업진흥원
sites.nipa_scan()

# sba
sites.sba_scan()

# kisa
sites.kisa_scan()

# Nia
sites.nia_scan()

# 한국정보통신 진흥원
sites.kdata_scan()

# 고용노동부
sites.moel_scan()

# 부산경제진흥원
sites.bepa_scan()

# 창업보육센터 네트워크시스템
sites.bi_scan()


sys.stdout.close()

driver = webdriver.Chrome('C:/chromedriver', options=options)
sys.stdout = open('output.txt', 'w')

# 과학기술정보통신부
sites.msit_scan(driver,standard_date)

# 창업진흥원
sites.kised_scan(driver,standard_date)

# 부산정보산업진흥원
sites.busanit_scan(driver, standard_date)

# K-스타트업 (창업넷)
sites.kstartup_scan(driver, standard_date)


# 출력결과 저장
sys.stdout.close()

# 결과물 DB 저장
mongo.store()

# 디비 닫기
mongo.close()

# file 저장
mongo.result()

# file 내용 메일 보내기
gmail.sendmail()

# 창닫기
driver.close()


sys.exit()

