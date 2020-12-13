import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject']='Automated Hiring Email Scammers'
msg['From']='Automation Hiring Scammers'
msg['To']='rawsmondoilandgas@gmail.com,career@rawsmondgasoil.ga'

with open('EmailTemplate') as myfile:
    data = myfile.read()
    msg.set_content(data)

for x in range(100):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("fathfdhdfhfdihucsc@gmail.com", "fathisgdgsdgsdgh@32423432")
        server.send_message(msg)

print("Email has been sent")






