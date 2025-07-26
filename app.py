from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    email = None
    if request.method == 'POST':
        email = request.form.get('email')
        print(f"New subscriber: {email}")  # Replace with real storage
    return render_template('index.html', email=email)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)