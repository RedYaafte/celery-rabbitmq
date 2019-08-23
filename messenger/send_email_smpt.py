import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.conf import settings

msg = MIMEMultipart('alternative')

msg['Subject'] = "Hello from Mandrill, Python style!"
# Your from name and email address
msg['From'] = "Yafté Muñoz <yafte@bedu.org>"
msg['To'] = "redyafte@gmail.com"

text = "Mandrill speaks plaintext"
part1 = MIMEText(text, 'plain')

html = "<em>Mandrill speaks <strong>HTML</strong></em>"
part2 = MIMEText(html, 'html')

username = settings.MANDRILL_USERNAME
password = settings.MANDRILL_APIKEY

msg.attach(part1)
msg.attach(part2)

s = smtplib.SMTP('smtp.mandrillapp.com', 587)

s.login(username, password)
s.sendmail(msg['From'], msg['To'], msg.as_string())
print(s)

s.quit()
