import smtplib
from email.mime.text import MIMEText
# Email credentials and details
sender_email = "mahdi.engr@gmail.com"  # Replace with your email address
app_password = "unvq oomn myrn gdua"  # Replace with the generated App Password
receiver_email = "mashihoor@gmail.com"
# The text to send
# test_string = "This is a super text"
with open("testfile.txt", "r") as file:
    email_content = file.read()


# Create the email message
msg = MIMEText(email_content)
msg["Subject"] = "Python Homework: Demo Text"
msg["From"] = sender_email
msg["To"] = receiver_email
# Use SMTP_SSL for a secure connection on port 465
server=smtplib.SMTP_SSL("smtp.gmail.com", 465) 
server.login(sender_email, app_password)
server.sendmail(sender_email, receiver_email, msg.as_string())
print("Email sent successfully!")


# Connect to Gmail's SMTP server and send the email
# try:
#     # Use SMTP_SSL for a secure connection on port 465
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#         server.login(sender_email, app_password)
#         server.sendmail(sender_email, receiver_email, msg.as_string())
#     print("Email sent successfully!")
# except Exception as e:
#     print(f"Error: {e}")
