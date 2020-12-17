import smtplib
from email.message import EmailMessage
from datetime import datetime

cd = datetime.today().strftime('%Y-%m-%d')

LOG = open('covid_raport.txt')
DATA = LOG.read()

passfrom = 'hasło do poczty'

fromaddr = 'pomoc@niemczok.pl'
toaddr = 'biuro@tmask.pl'

try:

    msg = EmailMessage()
    msg['From'] = fromaddr
    msg['Subject'] = 'Raport World – %s' % cd
    msg['To'] = toaddr
    msg.set_content(DATA)

    s = smtplib.SMTP('ssl0.ovh.net', 587)
    s.login(fromaddr, passfrom)
    s.send_message(msg)
    s.quit()
    print(f'Mail wysłany do: {toaddr}')
except:
    print(f'Błąd wysyłania :( do: {toaddr}')