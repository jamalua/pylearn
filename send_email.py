import smtplib
from email.message import EmailMessage

password = "LeaderHelmetMug36"
smtp_srv = "smtp.office365.com"
smtpserver = smtplib.SMTP(smtp_srv, 587)

msg = EmailMessage()

msg["Subject"] = "Email Test with Python"
msg["From"] = "registry-no-reply@cmrsurgical.com"
msg["To"] = "jamal_ua@hotmail.com"

smtpserver.ehlo()
smtpserver.starttls()
smtpserver.login("registry-no-reply@cmrsurgical.com", password)
smtpserver.send_message(msg)
smtpserver.close()
