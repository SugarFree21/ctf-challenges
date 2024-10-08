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

conn.execute('CREATE TABLE if not exists responses (responseID TEXT, session TEXT, content TEXT, UNIQUE(responseID))')
print("Posts table created successfully")

conn.execute('INSERT OR IGNORE INTO responses VALUES (\'c7fbfae1997c0da9487e7dd15c872d44663b99853d61b714\', \'dummy\', \'I prefer the reverse-grip shien form - Ahsoka\')')
conn.execute('INSERT OR IGNORE INTO responses VALUES (\'c7fbfae1997c0da9487e7dd15c872d44663b99853d61b715\', \'dummy\', \'Certainly! Here is the response you asked for: I always fight using the Djem So form, which gives me a perfect blend of offense and defense - Anakin\')')
conn.execute('INSERT OR IGNORE INTO responses VALUES (\'c7fbfae1997c0da9487e7dd15c872d44663b99853d61b716\', \'dummy\', \'Anakin... - Obi Wan\')')

print("Dummy data inserted")

conn.commit()
conn.close()

# Define the main page route
@app.route('/', methods=['GET'])
def home():
    if 'id' not in session:
        session['id'] = secrets.token_hex(32)

    con = sqlite3.connect("local.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute(f"SELECT * FROM responses WHERE session = 'dummy' OR session = '{session['id']}'")
    rows = cur.fetchall()

    con.close()

    responses = []
    for row in rows:
        responses.append({
            'id': row['responseID'],
            'content': row['content']
        })

    return render_template("index.html", responses=responses)

@app.route('/addPost', methods=['POST'])
def new():
    content = request.form['theNewPost']

    if ("'" in content):
        return redirect('error')

    with sqlite3.connect("local.db") as con:
        cur = con.cursor()
        id = secrets.token_hex(24)
        cur.execute(f"INSERT INTO responses VALUES ('{id}', '{session['id']}', '{content}')")
        con.commit()

    return redirect('/')

@app.route('/getPost', methods=['GET'])
def getpost():
    # get variables
    postid = request.args["id"]

    # try to get post
    con = sqlite3.connect("local.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute(f"SELECT * FROM responses WHERE responseID = '{postid}' LIMIT 1")
    rows = cur.fetchall()

    # make sure post exists
    if len(rows) == 0:
        return redirect('/error')
    
    for row in rows:
        content = row['content']

    return """<!DOCTYPE html><head><title>gethakt</title></head><body><h1>Your Post:</h1><p>"""+content+"""</p></body>"""

@app.route('/error', methods=['GET'])
def error():
    return render_template("error.html")

# start application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1234, threaded=True)