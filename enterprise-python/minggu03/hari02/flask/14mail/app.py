from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'asmbrt@gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'adisaputrodwi27@gmail.com'
app.config['MAIL_PASSWORD'] = '115126adi'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route("/")
def index():
    msg = Massage('Hello', sender = 'adisaputrodwi27@gmail.com', recipients = ['id1@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-mail"
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
    app.run(debug = True)