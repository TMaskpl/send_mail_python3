import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

cd = datetime.today().strftime('%Y-%m-%d')

passfrom = 'hasło do poczty'

fromaddr = 'pomoc@niemczok.pl'
toaddr = 'biuro@tmask.pl'

try:

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = ("Raport txt  %s" % cd)

    body = "Raport w załączniku"

    msg.attach(MIMEText(body, 'plain'))

    filename = "raport.txt"
    attachment = open('covid_raport.txt', "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('ssl0.ovh.net', 587)
    server.starttls()
    server.login(fromaddr, passfrom)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print(f'Mail wysłany do: {toaddr}')
except:
    print(f'Błąd wysyłania :( do: {toaddr}')
