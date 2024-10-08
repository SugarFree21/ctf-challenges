from flask import Flask, render_template, session, request, redirect
import secrets
import sqlite3
import re

# set up the web server
app = Flask(__name__)
app.secret_key = open("secret_key.txt", "r").read()
app.config["SESSION_COOKIE_HTTPONLY"] = False

# set up the database
conn = sqlite3.connect('local.db')
print("Opened database successfully")

conn.execute('CREATE TABLE if not exists users (username TEXT, passwd TEXT, UNIQUE(username))')
print("Users table created successfully")

conn.execute('INSERT OR IGNORE INTO users VALUES (\'darthvader\', \'byuctf{who_makes_their_password_a_flag?}\')')
conn.execute('INSERT OR IGNORE INTO users VALUES (\'tarkin\', \'intergalacticdomination\')')
conn.execute('INSERT OR IGNORE INTO users VALUES (\'wullfyularen\', \'remembercreekpath\')')

print("Dummy data inserted")

conn.commit()
conn.close()

# Define the main page route
@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def logmein():
    username = request.form['usernm']
    password = request.form['passwd']

    con = sqlite3.connect("local.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute(f"SELECT * FROM users WHERE username = '{username}' AND passwd = '{password}'")
    rows = cur.fetchall()

    con.close()

    if len(rows) == 0:
        return "invalid username or password"

    return render_template("admin.html", username=rows[0]['username'], password=rows[0]['passwd'])

@app.route('/error', methods=['GET'])
def error():
    return render_template("error.html")

# start application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1234, threaded=True)