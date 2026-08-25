import smtplib
from email.mime.text import MIMEText

EMAIL_USER = "3branwell@gmail.com"
# 아래에 새로 발급받은 16자리 앱 비밀번호를 넣으세요
EMAIL_PASS = "jsko fjyz xvrf cyqi"

def send_email():
    msg = MIMEText("테스트 메일입니다.")
    msg['Subject'] = "🚨 [테스트] CGV 용산 IMAX 알림 테스트!"
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_USER

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASS)
    server.sendmail(EMAIL_USER, EMAIL_USER, msg.as_string())
    server.quit()

if __name__ == "__main__":
    send_email()
