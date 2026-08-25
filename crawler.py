import os
import smtplib
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup

# [보안 설정] GitHub Secrets에서 로그인 정보 로드
GMAIL_ID = os.environ.get("GMAIL_ID")
GMAIL_APP_PW = os.environ.get("GMAIL_APP_PW")

def send_alert_email():
    """
    [기능] IMAX 회차 감지 시 지메일로 경보 메일을 보내는 함수
    - SSL 보안 연결(포트 465)을 통해 구글 서버에 안정적으로 접속합니다.
    """
    if not GMAIL_ID or not GMAIL_APP_PW:
        print("❌ [오류] GMAIL_ID 또는 GMAIL_APP_PW 변수를 찾을 수 없습니다.")
        return

    subject = "[🚨CGV 알림] 용산아이파크몰 9/2 IMAX 예매 오픈!"
    body = (
        "기다리시던 CGV 용산아이파크몰 9월 2일 IMAX 회차가 오픈되었습니다!\n\n"
        "지금 즉시 CGV 앱 또는 웹사이트에서 예매를 진행하세요!\n"
        "http://www.cgv.co.kr/ticket/"
    )

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = GMAIL_ID
    msg['To'] = GMAIL_ID

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(GMAIL_ID, GMAIL_APP_PW)
            server.sendmail(GMAIL_ID, GMAIL_ID, msg.as_string())
        print("✅ [발송 완료] 성공적으로 경보 메일을 전송했습니다.")
    except Exception as e:
        print(f"❌ [메일 오류] 메일 전송 중 예외 발생: {e}")

def check_cgv_imax():
    """
    [기능] CGV 용산아이파크몰 9/2 IMAX 상영관 생성 여부를 검사하는 함수
    """
    # CGV 용산아이파크몰(극장코드: 0013), 날짜: 2026년 9월 2일 타임테이블 URL
    url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatrcode=0013&date=20260902"
    
    # 봇 차단 방지용 User-Agent 브라우저 헤더 설정
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        # 정상적으로 페이지를 불러왔는지 상태 코드(200 OK) 확인
        if response.status_code != 200:
            print(f"⚠️ CGV 서버 응답 이상 (상태 코드: {response.status_code})")
            return

        soup = BeautifulSoup(response.text, 'html.parser')

        # CGV 타임테이블 내부의 IMAX 상영관 표시 요소(<span class="imax">) 추출
        imax_hall = soup.select_one('span.imax')

        # 회차가 열렸을 때만 조건문 진입
        if imax_hall:
            print("🎉 [감지 성공] 용산 CGV 9/2 IMAX 회차가 열렸습니다! 메일을 전송합니다.")
            send_alert_email()
        else:
            print("⏳ [미오픈] 아직 9/2 IMAX 회차가 열리지 않았습니다. 다음 주기(4분 뒤)에 재확인합니다.")

    except Exception as e:
        print(f"❌ [크롤링 오류] 사이트 접속 중 오류 발생: {e}")

if __name__ == "__main__":
    check_cgv_imax()
