import smtplib
from email.mime.text import MIMEText

EMAIL_USER = "3branwell@gmail.com"
EMAIL_PASS = "nfwjodvpugdhguqn"

def send_test_email():
    # 받는 메일 주소를 네이버 등 다른 메일로 변경해 봅니다.
    target_email = "jellyjoa09@naver.com" 

    msg = MIMEText("이 메일이 도착했다면 알림 서버 연동 성공입니다!")
    msg['Subject'] = "🚨 [테스트] CGV 용산 IMAX 알림 테스트!"
    msg['From'] = EMAIL_USER
    msg['To'] = target_email

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, target_email, msg.as_string())
        server.quit()
        print("메일 발송 완벽 성공!")
    except Exception as e:
        # 실패 시 에러 내용을 화면에 강제로 출력합니다.
        print(f"발송 실패 원인 에러: {e}")

if __name__ == "__main__":
    send_test_email()
