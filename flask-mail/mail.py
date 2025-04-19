from flask import Flask
from flask_mail import Mail, Message
from config import mail_password

def create_app():
    app = Flask(__name__)

    # Load configuration from a file or environment variables
    app.config['MAIL_SERVER'] = 'smtp.fastmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = 'randomtestsupport@fastmail.com'
    app.config['MAIL_PASSWORD'] = mail_password
    app.config['MAIL_DEFAULT_SENDER'] = ('John Doe','randomtestsupport@fastmail.com')
    app.config['MAIL_MAX_EMAILS'] = 5

    mail = Mail()
    mail.init_app(app)

    @app.route('/')
    def index():
        msg = Message('This is the Title!', recipients=['miweg27399@dpcos.com'])
        msg.body = 'This is the body of the email.'
        msg.html = '<h1>Please find attached.</h1>'

        with app.open_resource('test.pdf') as pdf:
            msg.attach('test.pdf', 'application/pdf', pdf.read())

        mail.send(msg)

        return '<h1>Message sent!</h1>'

    @app.route('/bulk')
    def bulk():
        users = [{'name': 'John Doe', 'email': 'johndoe@gmail.com'}]

        with mail.connect() as conn:
            for user in users:
                message = Message(subject='This is the Subject!',
                                  sender=app.config['MAIL_DEFAULT_SENDER'],
                                  recipients=[user['email']],
                                  body=f'Hello {user["name"]}!')
                conn.send(message)

    return app