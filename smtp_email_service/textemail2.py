import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject']='Automated Test Email'
msg['From']='Automation Testing'
msg['To']='fathihucsc@gmail.com'
msg['To']='career@rawsmondgasoil.ga,rawsmondoilandgas@gmail.com'

with open('EmailTemplate') as myfile:
    data = myfile.read()
    msg.set_content(data)


with open("Mr.Scammer.png","rb") as f:
    file_data=f.read()
    print("File data in binary",file_data)
    file_name = f.name
    print("File name is", file_name)
    msg.add_attachment(file_data,maintype="application", subtype="png",filename=file_name)


for x in range(1):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("fathihuasfdasfascsc@gmail.com", "sgsdgsdsdfsdg")
        server.send_message(msg)

print("Email has been sent")





