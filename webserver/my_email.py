import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


EMAIL_NAME = "gutomicsatlas@zohomail.com"
EMAIL_PASSWORD = "GutOmicsAtlasCornell1@"


def send_email(receiver: str, subject: str, content: str):
    message = MIMEMultipart()
    message["From"] = EMAIL_NAME
    message["To"] = receiver
    message["Subject"] = subject
    message.attach(MIMEText(content, "plain"))
    server = smtplib.SMTP("smtp.zoho.com", 587)
    server.starttls()
    server.login(EMAIL_NAME, EMAIL_PASSWORD)
    server.sendmail(EMAIL_NAME, receiver, message.as_string())
    server.quit()

if __name__ == '__main__':
    send_email('1246jtc@gmail.com', 'Test', 'This is a test email')
