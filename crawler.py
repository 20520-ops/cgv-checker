import os
import smtplib
from email.mime.text import MIMEText

EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_PASS = os.environ.get("EMAIL_PASS")

def send_email(subject, content):
    if EMAIL_USER and EMAIL_PASS:
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = EMAIL_USER
        msg['To'] = EMAIL_USER

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, EMAIL_USER, msg.as_string())

if __name__ == "__main__":
    # 무조건 메일 발송
    send_email(
        "🚨 [테스트] CGV 용산 IMAX 알림 테스트!",
        "이 메일이 지메일함에 도착했다면 모든 알림 연결이 완벽히 성공한 것입니다!"
    )
