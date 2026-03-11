import smtplib
from email.message import EmailMessage

def send_email(summary, recipient):

    msg = EmailMessage()
    msg["Subject"] = "Sales Insight Summary"
    msg["From"] = "yourgmail@gmail.com"
    msg["To"] = recipient
    msg.set_content(summary)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("yourgmail@gmail.com", "your_app_password")
        server.send_message(msg)