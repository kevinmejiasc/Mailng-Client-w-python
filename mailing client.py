#iMPORT LIBRERIES
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# Mail server (I used GMAIIL)
server = smtplib.SMTP('smtp.gmail.com', 465)

server.ehlo()

#You can wirte your password and have it in plain sight but I recomned to have it in a encrypted file.
with open('password.txt', 'r') as f:
    password = f.read()

#server login information
server.login('enteryouremail@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'CYBER_KEV'
msg['To'] = 'recipentemail@mail.com'
msg['Subject'] = 'Test'

#opening text file which contain text that I want to have into my email.
with open('email.txt', 'r') as f:
    message = f.read()

#attaching text to my email
msg.attach(MIMEText(message, 'plain'))

#sending email.
text = msg.as_string()
server.sendmail('enteryouremail@gmail.com', 'recipentmail@mail.com', text)

