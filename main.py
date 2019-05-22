from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import sites
import mongo, message
import sys
# 13개 사이트 16개 정보저장
sys.stdout = open('result.txt', 'w',encoding='UTF8')

date = datetime.now().strftime('%Y-%m-%d %H:%M')
print(date + ' 실행결과\n\n')

# 크롬드라이버의 추가 옵션을 설정하는 함수
options = Options()
options.add_argument('--kiosk')
# options.add_argument('headless')    # 창이 안보이게 돌리기

# ---------------------------- 동적인 웹 -----------------------
'''
    msit, 
    kstartup
    seoul
    venture
    ccei
'''
driver = webdriver.Chrome('C:/chromedriver', options=options)

# 과학기술정보통신부
sites.msit_scan(driver)

# K-스타트업 (창업넷)
sites.kstartup_scan(driver)

# 서울특별시 - 관련공고가 적으므로 잠시 제외
# sites.seoul_scan(driver)

# 벤처기업협회
sites.venture_scan(driver)

# 벤처기업협회
sites.ccei_scan(driver)

# 창닫기
driver.close()

# ----------------- 정적인 웹 크롤링 ---------------------------
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

# 고용노동부 - 관련공고가없어 제외
# sites.moel_scan()

# 부산경제진흥원
sites.bepa_scan()

# 창업보육센터 네트워크시스템
sites.bi_scan()

# 창업진흥원
sites.kised_scan()

# 부산정보산업진흥원
sites.busanit_scan()

# 산업통상자원부
sites.motie_scan()

# 서울창업허브
sites.seoulstartuphub_scan()

# 한국산업진흥협회
sites.koita_scan()

# 정보통신정책연구원
sites.kisdi_scan()

# 지능정보산업협회
sites.kai_scan()

# 부산광역시
sites.busan_scan()

# 한국인공지능협회
sites.koraia_scan()

# 아이디어마루
sites.ideamaru_scan()

# 부산테크노파크_사업공고
sites.btp_scan()

# 서울기업지원센터
sites.sbsc_scan()

# 중소벤처기업부
sites.mss_scan()

sys.stdout.close()

# 출력결과 저장
sys.stdout.close()

# 디비 닫기
mongo.close()

# file 내용 push
message.telegram_push()

sys.exit(0)
