import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

def reduce_day_count_and_send_email():
    global day_count
    day_count -=1

    logging.info(f"Day count reduced. Current day count: {day_count}")

    sender_email = "venky21798@gmail.com"
    receiver_email_venky = "venky21798@gmail.com"
    receiver_email_asha = "ashabaskar4@gmail.com"
    password = "v8015137566"

    subject = "Daily Update for Marriage"
    body = f"Day count Reduced.current day count: {day_count}"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email_venky,receiver_email_asha
    message["Subject"] = subject
    message.attach(MIMEText(body,"Plain"))

    with smtplib.SMTP("smtp.gmai.com",587) as server:
        server.starttls()
        server.login(sender_email,password)
        text = message.as_string()
        server.sendmail(sender_email,receiver_email_asha,receiver_email_venky,text)
if __name__ == "__main__":
    logging.basicConfig(filename="C:/Users/venky_5ea6nmj/PycharmProjects/pythonProject/pythonProject/KDF/engine/mrge_count.py",level=logging.INFO)
    day_count = 248

    reduce_day_count_and_send_email()