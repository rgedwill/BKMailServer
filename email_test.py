# from smtp_server import send_email

# send_email('UnitedStates.ReliableLoans', 'unitedstatesreliableloans', 'ryangedwill@gmail.com', 'it works!!!', 'THE BODY WORKS TOO')

def send_email(user, pwd, recipient, subject, body):
    import smtplib, ssl

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body
    port = 465  # For SSL





    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        # TODO: Send email here
        server.ehlo()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')

send_email('ryangedwill@gmail.com', 'GSim1234!', 'ryangedwill@gmail.com', 'sub', 'bod! </br><a href=\'http://www.google.com\'>click here</a>')
