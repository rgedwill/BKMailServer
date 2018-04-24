import smtplib

client = smtplib.SMTP('localhost')

fromaddr = 'your_email@somedomain.com'
toaddrs = 'your_friend@somedomain.com'
msg = 'Hello'

client.sendmail(fromaddr, toaddrs, msg)
client.quit()
