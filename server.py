import os
import csv
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/<string:page_name>')
def my_home(page_name):
    return render_template(page_name)


def data_writer(data):
    if not os.path.exists ("basedd.csv"):
        with open("basedd.csv", mode="a", newline="") as datab2:
            file = csv.writer(datab2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file.writerow(['email', 'subject', 'message'])

    with open("basedd.csv", mode="a", newline="") as datab2:
        file = csv.writer(datab2)
        email = data['email']
        subject = data['subject']
        message = data['message']
        file.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        data_writer(data)
        return render_template("thank.html")
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)
