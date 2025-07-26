from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    email = None
    if request.method == 'POST':
        email = request.form.get('email')
        print(f"New subscriber: {email}")  # Replace with real storage
    return render_template('index.html', email=email)

if __name__ == '__main__':
    app.run(debug=False, port=5000, host='127.0.0.1')
