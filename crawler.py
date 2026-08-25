import smtplib





from email.mime.text import MIMEText

EMAIL_USER = "3branwell@gmail.com"


EMAIL_PASS = "jskofjyzxvrfcyqi"

def send_email():
    
    
    msg = MIMEText("테스트 메일 전송 성공했습니다!")
 
    
    msg['Subject'] = "🚨 [테스트] CGV 용산 IMAX 알림 테스트!"
    
    
    msg['From'] = EMAIL_USER
    
    
    msg['To'] = EMAIL_USER

    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    
    server.starttls()
    
    
    server.login(EMAIL_USER, EMAIL_PASS)
    
    
    server.sendmail(EMAIL_USER, EMAIL_USER, msg.as_string())
    
    
    server.quit()
    
    
    
    print("메일 전송 성공!")

if __name__ == "__main__":
    send_email()
