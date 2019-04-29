import re, time
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import mongo
import ssl
from urllib.request import urlopen

today = datetime.now()

# ----------------- 정적인 웹 크롤링 ---------------------------
''' 
kotra, nipa, sba, kisa, nia, kdata, moel, bepa
'''


def kotra_scan():
    # 코트라 사이트
    name = 'Kotra'
    url = 'http://www.kotra.or.kr'
    # 신청가능 사업 공지
    req = requests.get('http://www.kotra.or.kr/kh/business/busiList.do?menuDiv=1&MENU_CD=T0501&TOP_MENU_CD=T0500&boardType=0')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    # selector 로 데이터가저오기
    titles = soup.select('td > a')
    dates = soup.select('tr > td:nth-child(3)')

    # 체크포인트 불러오기, 저장하기
    check_point_date = mongo.check_point_read(name)['save_date']
    mongo.check_point_save(name, titles[0].text)

    # 데이터 변수로 받아서 txt 저장
    for i in range(len(titles)):
        title = titles[i].text
        link = url + titles[i].get('href').split('\'').pop(1)
        date = dates[i].text
        sdate = date.split(" ~ ").pop(0)
        edate = date.split(" ~ ").pop(1)
       
        if check_point_date >= sdate:
            continue
        else:
            mongo.post_save(name, title, link, sdate, edate)
            print('이름: ' + name + '\n제목: ' + title + '\n링크: ' + link + '\n신청기간: ' + date + '\n')


def nipa_scan():
    # 정보통신 산업진흥원 url
    names = ['정보통신산업진흥원1', '정보통신산업진흥원2']
    url = 'http://www.nipa.kr'
    uris = ['', '/biz/']
    urls = ['http://www.nipa.kr/board/boardList.it?boardNo=103&menuNo=32&page=1',
            'http://www.nipa.kr/biz/bizNotice.it?menuNo=18&page=1']

    # 신청가능 사업 공지
    for j in range(2):
        req = requests.get(urls[j])
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        # selector 로 데이터가저오기
        titles = soup.select('td > a')
        dates = soup.select('tr > td.date')

        # 체크포인트 불러오기, 저장하기
        check_point = mongo.check_point_read(names[j])['title']
        mongo.check_point_save(names[j], titles[0].text)

        # 데이터 변수로 받아서 txt 저장
        for i in range(len(titles)):
            title = titles[i].text
            link = url + uris[j] + titles[i].get('onclick').split('\'').pop(1)
            date = dates[i].text

            if check_point == title:
                break
            else:
                mongo.post_save(names[j], title, link, date, '')
                print('이름: ' + names[j] + '\n제목: ' + title + '\n링크: ' + link + '\n등록일: ' + date + '\n')


def sba_scan():
    name = '서울산업진흥원'
    # 서울 산업 산업진흥원 url
    url = 'http://www.sba.seoul.kr/kr/sbcu01l1'
    # 신청가능 사업 공지
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    # selector 로 데이터가저오기
    titles = soup.select('td > a')
    dates = soup.select('tr > td:nth-child(3)')

    # 체크포인트 불러오기, 저장하기
    check_point = mongo.check_point_read(name)['title']
    mongo.check_point_save(name, titles[0].text.strip())

    # 데이터 변수로 받아서 txt 저장
    for i in range(len(titles)):
        title = titles[i].text.strip()
        seq = re.findall("\d+", titles[i].get('onclick'))
        link = "http://www.sba.seoul.kr/kr/sbcu01s1?bseq=" + seq[0]
        date = dates[i].text

        if check_point == title:
            break
        else:
            mongo.post_save(name, title, link, date, '')
            print('이름: ' + name + '\n제목: ' + title + '\n링크: ' + link + '\n등록일: ' + date + '\n')


def kisa_scan():
    # 한국인터넷진흥원 사이트
    name = '한국인터넷진흥원'
    url = "https://www.kisa.or.kr"
    # 신청가능 사업 공지
    req = requests.get('https://www.kisa.or.kr/notice/notice_List.jsp')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    # selector 로 데이터가저오기
    titles = soup.select('td > a')
    dates = soup.select('tr > td:nth-child(3)')

    # 체크포인트 불러오기, 저장하기
    check_point = mongo.check_point_read(name)['title']
    mongo.check_point_save(name, titles[0].text.strip())

    # 데이터 변수로 받아서 txt 저장
    for i in range(len(titles)):
        title = titles[i].text.strip()
        link = url + titles[i].get('href')
        date = dates[i].text.strip()

        if check_point == title:
            break
        else:
            mongo.post_save(name, title, link, date, '')
            print('이름: ' + name + '\n제목: ' + title + '\n링크: ' + link + '\n등록일: ' + date + '\n')


def nia_scan():
    name = '한국정보화진흥원'

    # 한국 정보화 진흥원 url
    url = 'https://www.nia.or.kr/site/nia_kor/ex/bbs/List.do?cbIdx=99835'

    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    # selector 로 데이터가저오기
    titles = soup.select('#sub_contentsArea > div.board_type01 > ul > li > a > span.subject')
    params = soup.select('#sub_contentsArea > div.board_type01 > ul > li > a')
    dates = soup.select('a > span.src > em:nth-child(1)')

    # 체크포인트 불러오기, 저장하기
    check_point = mongo.check_point_read(name)['title']
    mongo.check_point_save(name, " ".join(titles[0].text.split()))      # join과 split으로 중복 공백 제거

    # 데이터 변수로 받아서 txt 저장
    for i in range(len(titles)):
        title = " ".join(titles[i].text.split()) # join과 split으로 중복 공백 제거
        seq = re.findall('\d+', str(params[i].get('onclick')))
        link = "https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?cbIdx=" + seq[0] + "&bcIdx=" + seq[
            1] + "&parentSeq=" + seq[3]
        date = dates[i].text

        if check_point == title:
            break
        else:
            mongo.post_save(name, title, link, date, '')
            print('이름: ' + name + '\n제목: ' + title + '\n링크: ' + link + '\n등록일: ' + date + '\n')


def kdata_scan():
    name = '한국데이터산업진흥원'
    url = 'https://www.kdata.or.kr/board/notice_01.html'

    context = ssl._create_unverified_context()
    result = urlopen(url, context=context)
    soup = BeautifulSoup(result.read(), "html.parser")

    # selector 로 데이터가저오기
    titles = soup.select('td > a')
    dates = soup.select('tr > td.date')

    # 체크포인트 불러오기, 저장하기
    check_point = mongo.check_point_read(name)['title']
    mongo.check_point_save(name, titles[0].text.strip())

    # 데이터 변수로 받아서 txt 저장
    for i in range(len(titles)):
        title = titles[i].text.strip()
        link = 'https://www.kdata.or.kr/board/'+titles[i].get('href')
        date = dates[i].text

        if check_point == title:
            break
        else:
            mongo.post_save(name, title, link, date, '')
            print('이름: '+name + '\n제목: ' + title + '\n링크: ' + link + '\n등록일: ' + date + '\n')


def moel_scan():
    # 고용노동부 사이트
    name = '고용노동부'
    url = 'http://www.moel.go.kr'
    # 신청가능 사업 공지
    req = requests.get('http://www.moel.go.kr/info/govsupport/govsupportsub/govSupportSubList.do')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    # selector 로 데이터가저오기
    titles = soup.select('td > a')
    dates = soup.select('tr > td:nth-child(5)')

    # 체크포인트 불러오기, 저장하기
    check_point = mongo.check_point_read(name)['title']
    mongo.check_point_save(name, titles[0].text.split("]").pop(1).strip())

    # 데이터 변수로 받아서 txt 저장
    for i in range(len(titles)):
        title = titles[i].text.split("]").pop(1).strip()
        link = url + titles[i].get('href')
        date = dates[i].text

        if check_point == title:
            break
        else:
            mongo.post_save(name, title, link, date, '')
            print('이름: ' + name + '\n제목: ' + title + '\n링크: ' + link + '\n등록일: ' + date + '\n')


def bepa_scan():
    name = '부산경제진흥원'
    url = 'https://www.bepa.kr/kor/view.do?no=209'

    context = ssl._create_unverified_context()
    result = urlopen(url, context=context)
    soup = BeautifulSoup(result.read(), "html.parser")

    # selector 로 데이터가저오기
    titles = soup.select('td > a')
    dates = soup.select('tr > td.date')
    num = soup.select('td.num')

    # 체크포인트 불러오기
    check_point = mongo.check_point_read(name)['title']

    # 데이터 변수로 받아서 txt 저장
    for i in range(len(titles)):
        if (num[i].text != "NOTICE"):
            # 공지사항이 아닌 체크포인트 저장하기
            if (num[i-1].text == "NOTICE"):
                mongo.check_point_save(name, titles[i].text.strip().split('\n').pop(0))

            title = titles[i].text.strip().split("\n").pop(0)
            link = 'https://www.bepa.kr' + titles[i].get('href')
            date = dates[i].text

            if check_point == title:
                break
            else:
                mongo.post_save(name, title, link, date, '')
                print('이름: ' + name + '\n제목: ' + title + '\n링크: ' + link + '\n등록일: ' + date + '\n')


def bi_scan():
    # 창업보육센터 네트워크시스템 사이트
    name = '창업보육센터 네트워크시스템'
    url = ["http://www.bi.go.kr/board/editView.do?boardID=RECRUIT&frefaceCode=ANNOUNCE&boardVO.postSeq=", "&boardVO.registDate=", "&boardVO.viewFlag=view"]
    # 신청가능 사업 공지
    req = requests.get('http://www.bi.go.kr/board/list.do?boardID=RECRUIT&frefaceCode=ANNOUNCE')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    # selector 로 데이터가저오기
    titles = soup.select('td > a')
    dates = soup.select('tr > td:nth-child(5)')

    # 체크포인트 불러오기, 저장하기
    check_point = mongo.check_point_read(name)['title']
    mongo.check_point_save(name, titles[0].text.strip())

    # 데이터 변수로 받아서 txt 저장
    for i in range(len(titles)):
        title = titles[i].text.strip()
        params = re.findall("\d+", titles[i].get('href'))
        link = url[0] + params[0] + url[1] + params[1] + url[2]
        date = dates[i].text
        sdate = date.split(" ~ ").pop(0)
        edate = date.split(" ~ ").pop(1)

        if check_point == title:
            break
        else:
            mongo.post_save(name, title, link, sdate, edate)
            print('이름: ' + name + '\n제목: ' + title + '\n링크: ' + link + '\n신청기간: ' + date + '\n')


def kised_scan():
    # 창업진흥원 사이트
    name = '창업진흥원'

    # 신청가능 사업 공지
    req = requests.get('https://www.kised.or.kr/not/notice2.asp')
    req.encoding= 'euc-kr'
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    # selector 로 데이터가저오기
    titles = soup.select('td > a')
    dates = soup.select('tr > td:nth-child(4)')

    # 체크포인트 불러오기, 저장하기
    check_point = mongo.check_point_read(name)['title']
    mongo.check_point_save(name, titles[0].text)

    # 데이터 변수로 받아서 txt 저장
    for i in range(len(titles)):
        title = titles[i].text
        link = titles[i].get('href')
        date = dates[i].text
        if check_point == title:
            break
        else:
            mongo.post_save(name, title, link, date, '')
            print('이름: ' + name + '\n제목: ' + title + '\n링크: ' + link + '\n등록일: ' + date + '\n')


def busanit_scan():
    for j in range(2):
        names = ['부산정보산업진흥원_공지사항', '부산정보산업진흥원_사업공고']
        urls = ['http://busanit.or.kr/board/list.asp?bcode=notice_e','http://busanit.or.kr/board/list.asp?bcode=notice']

        # 신청가능 사업 공지
        req = requests.get(urls[j])
        req.encoding = 'utf-8'
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        # selector 로 데이터가저오기
        titles = soup.select('td > a')
        dates = soup.select('tr > td:nth-child(3)')

        # 체크포인트 불러오기, 저장하기
        check_point = mongo.check_point_read(names[j])['title']
        mongo.check_point_save(names[j], titles[0].text)

        # 데이터 변수로 받아서 txt 저장
        for i in range(len(titles)):
            title = titles[i].text
            link = 'http://busanit.or.kr/board/'+titles[i].get('href')
            date = dates[i].text
            if check_point == title:
                break
            else:
                mongo.post_save(names[j], title, link, date, '')
                print('이름: ' + names[j] + '\n제목: ' + title + '\n링크: ' + link + '\n등록일: ' + date + '\n')


# ---------------------------- 동적인 웹 -----------------------
'''
    msit, 
    kstartup
'''


def msit_scan(driver):
    name = '과학기술정보통신부'

    # 과학기술정보통신부 신청사업 url
    url = 'https://msit.go.kr/web/msipContents/contents.do?mId=MTE5'

    # 드라이버로 웹 열기
    driver.get(url)
    time.sleep(2)

    # 공지목록 가져오기
    boards_list = driver.find_elements_by_xpath('//*[@id="result"]/div[2]/div/table/tbody/tr')

    # 지난번 저장했던 포스트 가져오기
    check_point = mongo.check_point_read(name)['title']

    # 기준이될 point  저장
    mongo.check_point_save(name, boards_list[0].find_element_by_class_name('title').text)

    for x in boards_list:
        title = x.find_element_by_class_name('title').text
        if check_point != title:
            date = '20'+x.find_element_by_xpath('./td[3]/span/span[3]').text + '.' + x.find_element_by_xpath('./td[3]/span/span[2]').text
            link = x.find_element_by_tag_name('a').get_attribute('href')
            mongo.post_save(name, title, link, date,'')
            print('이름: ' + name + '\n제목:' + title + '\n링크: ' + link + '\n등록일: ' + date + '\n')
        else:
            break


def kstartup_scan(driver):
    name = 'kstartup'

    # k- startup 신청게시판 url
    url = 'http://www.k-startup.go.kr/common/announcement/announcementList.do?mid=30004&bid=701&searchAppAt=A'
    board_url = 'http://www.k-startup.go.kr/common/announcement/announcementDetail.do?mid=30004&bid=701&searchPrefixCode=BOARD_701_001&searchPostSn='

    # 드라이버로 웹 열기
    driver.get(url)

    # 페이지 다운버튼 누르기
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(2)

    # 지난번 저장했던 포스트 가져오기
    check_point = mongo.check_point_read(name)['title']
    point_flag = False

    pageCount = 1
    flag = False

    while pageCount < 10 and flag is False:

        # 페이지에 중요공지가 있을수도있고, 없을수도 있으니 try
        try:
            # 중요 공지 가져오기
            impo_board = driver.find_element_by_class_name('ann_list_impor')
            boards_list = impo_board.find_elements_by_xpath('./li')

            # 중요공지는 10개내외로 순차적이지않으므로, 제목을 비교하여 이전에것들을 제외시킨다.
            for x in boards_list:
                # 제목
                title = x.find_element_by_tag_name('a').text
                if mongo.is_saved(title) is None:
                    # 날짜 -  있는것과 없는것 구분처리
                    try:
                        due_date = re.findall("\d{4}-\d{2}-\d{2}", x.find_element_by_xpath('./ul/li[3]').text)
                        date = due_date[0]
                    except Exception:
                        date = "상시모집"

                    # link - bi.net_url, kstartup_url 구분처리
                    params = re.findall("\d+", x.find_element_by_tag_name('a').get_attribute('href'))
                    if len(params) == 2:  # bi-net 이동하는 함수일때, 파라미터가 2개임
                        link = "http://www.bi.go.kr/board/editView.do?boardVO.viewFlag=view&boardID=NOTICE&postSeq=" + \
                               params[0] + "&registDate=" + params[1]
                    elif len(params) > 2:
                        link = board_url + params[2]
                    else:
                        link = "링크오류"
                    mongo.post_save(name, title, link, '', date)
                    print('이름: ' + name + '\n제목:' + title + '\n링크: ' + link + '\n마감일: ' + date + '\n')
        except Exception:
            pass

        try:
            # 페이지별 공지 가져오기
            ann_board = driver.find_element_by_class_name('ann_list')
            boards_list2 = ann_board.find_elements_by_xpath('./li')
            if point_flag is False:
                mongo.check_point_save(name, boards_list2[0].find_element_by_tag_name('a').text)
                point_flag = True

            for x in boards_list2:
                title = x.find_element_by_tag_name('a').text
                if check_point != title:
                    # 날짜 있는것과 없는것 구분처리
                    try:
                        due_date = re.findall("\d{4}-\d{2}-\d{2}", x.find_element_by_xpath('./ul/li[3]').text)
                        date = due_date[0]
                    except Exception:
                        date = "상시모집"

                    #  bi.net_url, kstartup_url 구분처리
                    params = re.findall("\d+", x.find_element_by_tag_name('a').get_attribute('href'))
                    if len(params) == 2:  # bi-net 이동하는 함수일때, 파라미터가 2개임
                        link = "http://www.bi.go.kr/board/editView.do?boardVO.viewFlag=view&boardID=NOTICE&postSeq=" + \
                               params[0] + "&registDate=" + params[1]
                    elif len(params) > 2:
                        link = board_url + params[2]
                    else:
                        link = "링크오류"
                    mongo.post_save(name, title, link, '', date)
                    print('이름: ' + name + '\n제목:' + title + '\n링크: ' + link + '\n마감일: ' + date + '\n')
                else:
                    flag = True
                    break
        except Exception:
            pass

        # 페이지 이동
        driver.find_element_by_xpath(
            '// *[ @ id = "searchAnnouncementVO"] / div[2] / div[4] / a[' + str(pageCount) + ']').click()
        pageCount += 1


