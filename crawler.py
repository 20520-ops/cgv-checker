import os
import smtplib
from email.mime.text import MIMEText

print("CGV 티켓 확인 크롤러 실행 중...")

# 환경 변수 정상 로드 확인
gmail_id = os.environ.get("GMAIL_ID")
gmail_pw = os.environ.get("GMAIL_APP_PW")

if gmail_id and gmail_pw:
    print("지메일 계정 정보가 성공적으로 전달되었습니다.")
else:
    print("경고: GitHub Secrets에서 지메일 정보를 찾을 수 없습니다.")

print("테스트 완료!")
