from flask import Flask, request, render_template, render_template_string
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/login', methods=['GET'])
def login_form():
    form_html = '''
    <form method="POST" action="/login">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username">
        <label for="password">Password:</label>
        <input type="password" id="password" name="password">
        <input type="submit" value="Login">
    </form>
    '''
    return render_template_string(form_html)

#Route to hand form submission
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if not re.match(r"^[a-zA-Z0-9_-]+$", username):
        return "Invalid username. Please use only letters, numbers and underscores"

    if len(password) < 8:
        return "Invalid password. Password must be at least 8 characters long"

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    return f"""
        <h2>Login Successful</h2>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Hashed Password:</strong> {hashed_password}</p>
        """

if __name__ == '__main__':
    app.run(debug=True)


