from flask import render_template
from flask_mail import Message
from threading import Thread

# This class will hold the Mail instance and the app context
class EmailService:
    def __init__(self):
        self.mail = None
        self.app = None

    def init_app(self, app, mail):
        self.app = app
        self.mail = mail

    def _send_async_email(self, msg):
        """Helper function for sending email in a background thread."""
        with self.app.app_context():
            try:
                self.mail.send(msg)
                print(f"Email sent successfully to {msg.recipients}")
            except Exception as e:
                print("--- EMAIL SENDING FAILED ---")
                print(f"Error: {e}")
                print("----------------------------")

    def send_email(self, to, subject, template, **kwargs):
        """
        Sends an email.
        :param to: Recipient's email address.
        :param subject: Email subject.
        :param template: Path to the Jinja2 template for the email body.
        :param kwargs: Additional arguments to pass to the template.
        """
        if not self.app or not self.mail:
            raise RuntimeError("EmailService has not been initialized with a Flask app.")
        
        # We access the config directly from self.app
        msg = Message(
            f"CityLinkConnect- {subject}",
            sender=self.app.config['MAIL_DEFAULT_SENDER'],
            recipients=[to]
        )
        # We need the app context to render the template
        with self.app.app_context():
            msg.html = render_template(template, **kwargs)
        
        # Send email in a background thread
        thr = Thread(target=self._send_async_email, args=[msg])
        thr.start()
        return thr

# Create a single instance of our service that we can import elsewhere
email_sender = EmailService()