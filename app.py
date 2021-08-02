from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def homePage():
    return render_template('home.html')

@app.route('/market')
def market():
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
]
    return render_template('market.html' , item = items)












# @app.route('/about')
# def about(username):
#     return '<h1>THis is about page of {username}</h1>'

@app.route('/about/<username>')
def aboutu(username):
    return f'<h1>THis is about page of {username}</h1>'

if __name__ == '__main__':
    app.run()




# pip install virtualenv
# virtualenv env
# .\env\Scripts\activate