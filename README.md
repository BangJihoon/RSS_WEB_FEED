# 공고문 Crowlling 프로그램

기존의 selenium모듈의 webdriver를 이용한 크롤링은 Dom이 그려지고 나서 접근하므로, 시간이 느리고,
네트워크 환경에 따라 신뢰성이 떨어졌다.
selenium의 단점을 보완하고 성능을 향상시키고자 
웹 소스를 읽어와서 파싱하는 requests와 bs4를 이용하는 방법으로 변경해주었고,
JS웹은 동적생성되므로 기존의 selenium으로 크롤링을 진행하여, 
현재 혼합형식으로 구현되어있다.


# pip-requirements.txt
freeze 모듈을 이용하여 pip-requirements를 뽑아두었다. 		
[pip freeze > pip-requirements.txt]
pip-requirements.txt 를통해 한번에 필요한 모듈을 설치할수있다. 	
[pip install pip-requirements.txt] 


# chromedrive 다운
크롤링프로젝트 수정을 위해 C:안에 chromedrive가 필요하다.


# pyinstaller 를 이용한 실행파일 만들기 
main 을 실행파일로 만드는 방법				
[pyinstaller -F main.py]


# 기타 txt 파일생성
output은 크롤링하여 받아온 자료로 저장전 상태이며, 디비에 저장후, 가독성이 좋은 result.txt 를 만든다
저장후 정리된자료는 result는 메일로 보내준다.
