import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(receiver_email, subject, body):
    sender_email = "your_email@gmail.com"
    password = "your_password"

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to the message
    message.attach(MIMEText(body, "plain"))

    # Connect to the Gmail SMTP server and send the email
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print("Error: unable to send email. Error message:", e)

# Example usage
send_email("receiver@example.com", "Test Subject", "This is a test message.")

