import os
import smtplib
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup
from flask import Flask

# Flask 웹 서버 생성
app = Flask(__name__)

# Render 환경 변수에서 보안 변수 불러오기 (기존 GitHub Secrets 역할)
GMAIL_ID = os.environ.get("GMAIL_ID")
GMAIL_APP_PW = os.environ.get("GMAIL_APP_PW")

def send_alert_email():
    """IMAX 회차가 열렸을 때 지메일로 즉시 경보 메일을 발송합니다."""
    if not GMAIL_ID or not GMAIL_APP_PW:
        print("❌ [보안 오류] GMAIL_ID 또는 GMAIL_APP_PW 변수가 설정되지 않았습니다.")
        return

    subject = "[🚨CGV 알림] 용산아이파크몰 9/2 IMAX 예매가 열렸습니다!"
    body = (
        "기다리시던 CGV 용산아이파크몰 9월 2일 IMAX 회차가 오픈되었습니다!\n\n"
        "지금 즉시 CGV 앱이나 웹사이트에 접속하여 예매를 진행하세요!\n"
        "http://www.cgv.co.kr/ticket/"
    )

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = GMAIL_ID
    msg['To'] = GMAIL_ID

    try:
        # SSL 보안 연결 (포트 465) 사용
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10) as server:
            server.login(GMAIL_ID, GMAIL_APP_PW)
            server.sendmail(GMAIL_ID, GMAIL_ID, msg.as_string())
        print("✅ [발송 완료] 성공적으로 경보 메일을 전송했습니다.")
    except Exception as e:
        print(f"❌ [메일 오류] 메일 전송 실패: {e}")

def check_cgv_imax():
    """CGV 용산아이파크몰 2026년 9월 2일 IMAX 회차 감시"""
    # CGV 용산(0013), 2026년 9월 2일 시간표 iframe URL
    url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatrcode=0013&date=20260902"
    
    # CGV 봇 차단 회피용 헤더 설정
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'http://www.cgv.co.kr/theaters/'
    }

    try:
        # 응답 대기 시간 15초 제한으로 무한 로딩 방지
        response = requests.get(url, headers=headers, timeout=15)
        
        # HTTP 응답 코드 검증
        if response.status_code != 200:
            print(f"⚠️ [서버 응답 이상] HTTP 상태 코드: {response.status_code}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')

        # CGV 타임테이블 상의 IMAX관 표시 태그
        imax_hall = soup.select_one('span.imax, i.imax, div.hall_imax')

        if imax_hall:
            print("🎉 [감지 성공] 용산 CGV 9/2 IMAX 회차가 열렸습니다! 이메일을 발송합니다.")
            send_alert_email()
        else:
            print("⏳ [미오픈] 아직 9/2 IMAX 회차가 열리지 않았습니다. 다음 주기에 재확인합니다.")

    except requests.exceptions.Timeout:
        print("⚠️ [타임아웃] CGV 서버 응답 시간이 초과되었습니다. 다음 주기에 다시 시도합니다.")
    except Exception as e:
        print(f"❌ [크롤링 오류] 예외 발생: {e}")

# 누군가(UptimeRobot)가 접속할 때마다 크롤링 실행!
@app.route('/')
def keep_alive():
    check_cgv_imax()
    return "서버가 정상 작동 중이며, CGV 용아맥을 확인했습니다!"

if __name__ == "__main__":
    # Render 환경에 맞게 포트 설정 후 서버 실행
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
