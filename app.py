from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'qwert'
app.config['MYSQL_DB'] = 'myusers'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstname = details['fname']
        lastname = details['lname']
        birthdate = details['birthday']
        gender = details['gender']
        email = details['email']
        phone = details['phone']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(firstname, lastname, gender, email, phone, birthdate) VALUES (%s, %s, %s, %s, %s, %s)", (firstname, lastname, gender, email, phone, birthdate))
        mysql.connection.commit()
        cur.close()
        return 'success'

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
