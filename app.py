from flask import Flask, render_template, request, redirect, url_for, session
import unicodedata

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        username = unicodedata.normalize('NFC', username)
        password = unicodedata.normalize('NFC', password)

        if username == '니하오유이풍' and password == '200(1234)':
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            error = "야!!! 죽을래???"

    return render_template('login.html', error=error)

@app.route('/home')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5005))
    app.run(host='0.0.0.0', port=port)