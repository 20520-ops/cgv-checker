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
    # 본인 지메일 주소 전체 (숫자 3 포함)
    msg['To'] = "3branwell@gmail.com"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, msg['To'], msg.as_string())
        server.quit()
        print("메일 발송 완료")
    except Exception as e:
        print(f"오류: {e}")

if __name__ == "__main__":
    send_email(
        "🚨 [테스트] CGV 용산 IMAX 알림 테스트!",
        "이 메일이 보인다면 알림연동 완벽 성공입니다!"
    )
