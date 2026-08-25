import os
import smtplib
from email.mime.text import MIMEText

EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_PASS = os.environ.get("EMAIL_PASS")

def send_email(subject, content):
    if not EMAIL_USER or not EMAIL_PASS:
        return

    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    # 알림을 실제로 받고 싶은 메일 주소를 아래 따옴표 안에 정확히 입력하세요
    msg['To'] = "3branwell@gmail.com"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, msg['To'], msg.as_string())
        server.quit()
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    send_email(
        "🚨 [테스트] CGV 용산 IMAX 알림 테스트!",
        "이 메일이 도착했다면 알림 연결 성공입니다!"
    )
