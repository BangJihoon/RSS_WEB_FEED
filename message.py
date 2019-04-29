# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from slacker import Slacker
import websocket
import mongo
import telegram

date = datetime.now().strftime('%Y-%m-%d %H:%M')


def sendmail():
    with open('result.txt', 'rt', encoding='UTF8') as file:
        contents = file.read()
        # ------------------ 메일보내기 https://yeolco.tistory.com/93 --- 참고

        # # 세션생성
        # s = smtplib.SMTP('smtp.gmail.com', 587)
        # # TLS 보안 시작
        # s.starttls()
        #
        # # 로그인 인증
        # s.login('jihoon289@gmail.com', 'opjjhvlrvidyfzdo')
        #
        # # 보낼 메시지 설정
        # msg = MIMEText(contents)
        # msg['Subject'] = date + ' 공고문 스크랩'
        #
        # # 메일 보내기 (보내는사람, 받을사람, 내용)
        # s.sendmail("jihoon289@gmail.com", "jihoon289@naver.com", msg.as_string())
        # s.sendmail("jihoon289@gmail.com", "mina312@naver.com", msg.as_string())
        # s.sendmail("jihoon289@gmail.com", "pakusepgame@gmail.com", msg.as_string())
        #
        # # 세션 종료
        # s.quit()


        # # slack 메세지 보내기
        # token = "xoxp-612642071956-608238527025-608321031505-4f7c38c1646cc67698aef010e2dd1b76"
        # slack = Slacker(token)
        #
        # num = mongo.count()
        # if num:
        #     slack.chat.post_message("#todays-posts", ("새로운 공고문이 " + str(num) + "개 올라왔습니다."))
        # else:
        #     slack.chat.post_message("#todays-posts", "새로운 공고문이 없습니다.")
        #
        # # slack.chat.post_message("#todays-posts",contents)

        API_KEY = '818222067:AAFJWKcasPwz2DPRZu6HSFmzv8CerHHsm_k'
        bot = telegram.Bot(token=API_KEY)
        #chat_id 확인 -> https://api.telegram.org/bot818222067:AAFJWKcasPwz2DPRZu6HSFmzv8CerHHsm_k/getUpdates
        chat_id = "-1001360438299"

        num = mongo.count()

        bot.sendMessage(chat_id=chat_id, text="새로운 공고문이 " + str(num) + "개 올라왔습니다. \n자세히 보기 : http://bvpost.shop/")

        chat_id = "-1001447356505"

        bot.sendMessage(chat_id=chat_id, text= contents)
