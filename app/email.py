from threading import Thread
from flask import current_app
from flask_mail import Message
from app import mail

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)
        app.logger.info('Successfully sent {0} a recovery email'.format(msg.recipients))


def send_email(subject, sender, recipients, text_body, html_body):
    current_app.logger.info('Sending email to {0} from {1}'.format(recipients, sender))
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email,
           args=(current_app._get_current_object(), msg)).start()
