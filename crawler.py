import smtplib
from email.mime.text import MIMEText

# 본인 계정 정보 직접 지정 (오류 원인 완벽 제거)
EMAIL_USER = "3branwell@gmail.com"
EMAIL_PASS = "nfwjodvpugdhguqn"

def send_test_email():
    msg = MIMEText("이 메일이 도착했다면 알림 연동 및 서버 연결 완벽 성공입니다!")
    msg['Subject'] = "🚨 [테스트] CGV 용산 IMAX 알림 테스트!"
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_USER

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, EMAIL_USER, msg.as_string())
        server.quit()
        print("메일 발송 완료!")
    except Exception as e:
        print(f"발송 실패 원인: {e}")

if __name__ == "__main__":
    send_test_email()
