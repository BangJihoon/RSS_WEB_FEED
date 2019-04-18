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

# 13개 사이트 16개 정보저장

sys.stdout = open('result.txt', 'w',encoding='UTF8')

date = datetime.now().strftime('%Y-%m-%d %H:%M')
print(date + ' 실행결과\n\n')

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

# 창업진흥원
sites.kised_scan()

# 부산정보산업진흥원
sites.busanit_scan()

sys.stdout.close()

driver = webdriver.Chrome('C:/chromedriver', options=options)
sys.stdout = open('output.txt', 'w')

# 과학기술정보통신부
sites.msit_scan(driver)

# K-스타트업 (창업넷)
sites.kstartup_scan(driver)

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

# print("\n\n\n--------------------- 실행 완료 -------------------------\n\n\n")

sys.exit(0)
