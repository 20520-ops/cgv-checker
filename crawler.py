import os
import smtplib
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup

THEATER_CODE = "0013"
TARGET_DATE = "20260902"
MOVIE_TITLE = "오디세이"

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

def check_open():
    url = f"http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode={THEATER_CODE}&date={TARGET_DATE}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        for imax in soup.select("span.imax"):
            container = imax.find_parent("div", class_="col-times")
            if container and container.find("a") and MOVIE_TITLE in container.find("a").text.strip():
                return True
    except Exception as e:
        print(f"오류: {e}")
    return False

if __name__ == "__main__":
    if check_open():
        send_email(
            f"🚨 [CGV 용산] 9/2일자 '{MOVIE_TITLE}' IMAX 예매 오픈!",
            f"예매가 오픈되었습니다. 지금 CGV 앱으로 접속하세요!"
        )
