import os
import smtplib
from email.mime.text import MIMEText

EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_PASS = os.environ.get("EMAIL_PASS")

def send_test_email(target_email):
    if not EMAIL_USER or not EMAIL_PASS:
        print("Secrets 설정 오류: EMAIL_USER 또는 EMAIL_PASS가 없습니다.")
        return

    msg = MIMEText("이 메일이 보인다면 알림 연동 성공입니다!")
    msg['Subject'] = "🚨 [테스트] CGV 용산 IMAX 알림 테스트!"
    msg['From'] = EMAIL_USER
    msg['To'] = target_email

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, target_email, msg.as_string())
        server.quit()
        print("메일 발송 성공!")
    except Exception as e:
        print(f"발송 실패 에러 내용: {e}")

if __name__ == "__main__":
    # 아래 따옴표 안에 메일 받을 지메일 주소를 직접 적어주세요!
    send_test_email("3branwell@gmail.com")
