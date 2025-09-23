import smtplib


import os
import zipfile

from datetime import datetime
from email.message import EmailMessage

def add_attachment(msg, filepath):
    with open(filepath, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="octet-stream",
                filename=os.path.basename(filepath),
            )
        

def send_email(sender, password, receiver, subject, body, single_file=None, multiple_files=None, folder_to_zip=None):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    # 1. Attach a single file
    if single_file:
        add_attachment(msg,single_file)
        print("Single file Attach")
    else:
        print("Not single file Attach")

    # 2.Attach multiple files
    if multiple_files:
        for file in multiple_files:
            add_attachment(msg,file)
        print("Multiple file Attach")
    else:
        print("Not Multiple file Attach")

    # 3. Zip a folder and attach
    if folder_to_zip:
        zip_filename = folder_to_zip + ".zip"
        with zipfile.ZipFile(zip_filename, "w") as zipf:
            for root, dirs, files in os.walk(folder_to_zip):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, folder_to_zip))
        with open(zip_filename, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="zip",
                filename=os.path.basename(zip_filename),
            )
        print("create zip file Attach")

    # Send email using Gmail SMTP
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)  # Use App Password for Gmail
        smtp.send_message(msg)
        print("Email sent successfully!")


# -------------------- USAGE --------------------

send_email(
    sender="mahdi.engr@gmail.com",
    password="unvq oomn myrn gdua",  
    receiver="mashihoor@gmail.com",
    subject="Test Email with Files",
    body="Please find attached files.",
    single_file="example.txt",  # one file
    multiple_files=["testfile.txt","mail_multiple_attach.py"],  # multiple files
    folder_to_zip="my_folder"  # whole folder
)
