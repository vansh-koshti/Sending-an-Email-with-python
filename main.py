import smtplib
import pyttsx3
from email.message import EmailMessage

engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    string = input("Enter ...")
    return string


def send_email(name, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('...', '...')

    email = EmailMessage()
    email['From'] = '...'
    email['To'] = name
    email['Subject'] = subject
    email.set_content(message)

    server.send_message(email)

def get_email_info():
    talk('To whom is the message being sent to?')
    name = get_info()
    talk(name)
    talk('What is the subject?')
    subject = get_info()
    talk(subject)
    talk('What is the message')
    message = get_info()
    talk(message)
    send_email(name, subject, message)


get_email_info()
