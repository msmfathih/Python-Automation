import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject']='Automated Test Email'
msg['From']='Automation Testing'
msg['To']='msmfathih40@gmail.com'
#msg.set_content("Marrage Proposal to Ashika")

with open('EmailTemplate') as myfile:
    data = myfile.read()
    msg.set_content(data)

for x in range(1):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("test@gmail.com", "2020")
        server.send_message(msg)

print("Email has been sent")




