# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from slacker import Slacker
import websocket


date = datetime.now().strftime('%Y-%m-%d %H:%M')


def sendmail():
    file = open('result.txt', 'rt', encoding='UTF8')
    contents = file.read()
    # ------------------ 메일보내기 https://yeolco.tistory.com/93 --- 참고

    # 세션생성
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # TLS 보안 시작
    s.starttls()

    # 로그인 인증
    s.login('jihoon289@gmail.com', 'opjjhvlrvidyfzdo')

    # 보낼 메시지 설정
    msg = MIMEText(contents)
    msg['Subject'] = date + ' 공고문 스크랩'

    # 메일 보내기 (보내는사람, 받을사람, 내용)
    s.sendmail("jihoon289@gmail.com", "jihoon289@naver.com", msg.as_string())
    s.sendmail("jihoon289@gmail.com", "mina312@naver.com", msg.as_string())
    s.sendmail("jihoon289@gmail.com", "pakusepgame@gmail.com", msg.as_string())

    # 세션 종료
    s.quit()

    # slack 메세지 보내기
    token = "xoxp-612642071956-615359344966-615029538087-b59ddaae7800a83383d9c7f37b40ae3c"
    slack = Slacker(token)
    slack.chat.post_message("#todays-posts",contents)
