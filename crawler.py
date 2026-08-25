import os
import smtplib
from email.mime.text import MIMEText

# 1. GitHub Secrets에서 설정한 환경 변수 가져오기
GMAIL_ID = os.environ.get("GMAIL_ID")
GMAIL_APP_PW = os.environ.get("GMAIL_APP_PW")

# 2. 메일 발송 함수
def send_test_email():
    print(f"지메일 ID 확인: {GMAIL_ID}")
    
    if not GMAIL_ID or not GMAIL_APP_PW:
        print("❌ 에러: GitHub Secrets에 GMAIL_ID 또는 GMAIL_APP_PW가 설정되지 않았습니다.")
        return

    # 메일 내용 작성
    subject = "[테스트 메일] CGV 크롤러 지메일 연동 테스트"
    body = "이 메일이 도착했다면 GitHub Actions와 Gmail SMTP 연동에 완전히 성공한 것입니다! 🎉"
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = GMAIL_ID
    msg['To'] = GMAIL_ID  # 나 자신에게 보내기

    try:
        # Gmail SMTP 서버를 통해 메일 전송
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_ID, GMAIL_APP_PW)
            server.sendmail(GMAIL_ID, GMAIL_ID, msg.as_string())
        print("✅ 테스트 이메일 발송 성공! 지메일함을 확인하세요.")
    except Exception as e:
        print(f"❌ 이메일 발송 실패: {e}")

if __name__ == "__main__":
    send_test_email()
