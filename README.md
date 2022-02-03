# 공고문 Crowlling 프로그램

```
학점연계형 인턴중 대표님께서 원하시는 업무를 자동화하기 위해 시작한 1인 사이드 프로젝트.

다양한 사이트에서 올라오는 국가지원사업 공고문을 한눈에 보기위해 만든 웹서비스
```

### 일시
+ 2019.03 ~2019.04

### 개발환경 및 언어
<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=Amazon&logoColor=white"/> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white"/> <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=MongoDB&logoColor=white"/>
<img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=Bootstrap&logoColor=white"/>


<br/>

### 릴리즈 

https://user-images.githubusercontent.com/26866859/152365402-36338f32-0846-4982-b47b-98c3e8e5793c.mp4

<br/>

### 개발 기능 
+ 평일 오전 10시기준 국가 공고문 게시 사이트들을 순회하는 프로그램 자동 동작
+ 신규 공고문에 대해서 키워드 알림된 공고문의 갯수를 확인후 알림
+ 사내 그룹웨어인 Slack과 Telegram을 통해 웹서비스 URL과 몇건의 신규공고문이 올라왔는지 자동메세지
+ 웹서비스로 제공하는 내용은 제목, 내용, 링크, 등록일자 등의 내용만을 받아와 싱글페이지로 제공


### 구현 설명 
+ BOOTSTRAP과 JS, AJAX를 이용해 비동기적이고 빠른 검색기능을 제공하는 웹 구성
+ Python Flask 이용해 서버 구축
+ Python WebDriver를 이용한 크롤링
+ 20 여개 국가사업 공고 사이트에서 신규 공고문에 대한 내용을 DBaaS인 MongoDB Atlas에 수집
+ ajax와 selvet을 활용한 js를 통해 비동기적인 조회와 접근이 가능하도록 웹 기능을 넣었다.</br>
+ 크롤링을 selenium모듈을 이용해서 Dom이 그려지고 나서 접근하도록 구성하니 전체 사이트 순회시간이 길고 느려
+ Selenium Library의 단점을 보완하고 성능을 향상시키고자 웹 소스를 읽어와서 파싱하는 Requests와 bs4를 추가적으로 이용하였다.
+ 동적으로 요청에 의해 웹이 랜더링되는 웹사이트를 제외하고, 서버사이드 언어가 아닌 정적인 웹의 경우는 후자를 이용했다.




<br/>
<br/>

#### P.S  
<details>
  <summary>코드 수행방법</summary>
  

#### pip-requirements.txt
+ freeze 모듈을 이용하여 pip-requirements를 뽑아두었다. 		
+ [pip freeze > pip-requirements.txt]
+ pip-requirements.txt 를통해 한번에 필요한 모듈을 설치할수있다. 	
+ [pip install pip-requirements.txt] 


#### chromedrive 다운
+ 크롤링프로젝트 수정을 위해 C:안에 chromedrive가 필요하다.


#### pyinstaller 를 이용한 실행파일 만들기 
+ main 을 실행파일로 만드는 방법				
+ [pyinstaller -F main.py]

#### 기타 txt 파일생성
+ output은 크롤링하여 받아온 자료로 저장전 상태이며, 디비에 저장후, 가독성이 좋은 result.txt 를 만든다
+ 저장후 정리된자료는 result는 메일로 보내준다.

  </details>
