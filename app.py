from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'kusumaranam@gmail.com'  # Your Gmail username (email address)
app.config['MAIL_PASSWORD'] = 'opaz klcs jeiw iirw'  # Your Gmail password or App Password
app.config['MAIL_DEFAULT_SENDER'] = 'kusumaranam@gmail.com'  # Your Gmail address


mail = Mail(app)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    # Get data from the form submission
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Create email message
    msg = Message(f"Message from {name} ({email})", recipients=['your_email@gmail.com'])
    msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

    try:
        mail.send(msg)
        return jsonify({'message': 'Your message has been sent successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
