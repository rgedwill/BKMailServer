# unitedstates.reliableloans@gmail.com
# unitestatesreliableloans
#
# deangelocheng@gmail.com
# deangelocheng1
def send_loan_email(user, pwd, recipient, company, body):
    import smtplib

    print("company: %s" % company)
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = 'Did you mention at bizzcon you needed a loan for %s?' % company
    TEXT = body

    # BEGIN MIME ATTEMPT
    # from email.mime.text import MIMEText
    # from email.mime.multipart import MIMEMultipart
    # msg = MIMEText('<a href="www.facebook.com">Wrked</a>')
    # msg['Subject'] = "something"
    # msg['From'] = FROM
    # msg['To'] = TO


    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        
        print("failed to send mail, check your username/password and ensure your internet connection is working")

