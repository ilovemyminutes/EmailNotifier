import smtplib
from email.mime.text import MIMEText


def notify():
    s = smtplib.SMTP('smtp.gmail.com', 587) # 587: Gmail 포트번호
    s.starttls() # Gmail 보안상 TLS 보안 시작
    # s.login('example@example.com', 'passwordpassword')

    msg = MIMEText('학습이 완료되었습니다.')
    msg['Subject'] = '[Notification] 학습이 완료되었습니다.'

    s.sendmail("silkstaff777@gmail.com", "silkstaff@naver.com", msg.as_string()) # 메일 보내기
    s.quit() # 세션 종료

if __name__ == '__main__':
    notify()