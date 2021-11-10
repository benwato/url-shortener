from flask import Flask, render_template, request
from flask_cors import CORS
from url_generator import generator
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(150), unique=True, nullable=False)
    shortened_url = db.Column(db.String(20), unique=True, nullable=False)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        url = request.form['url-input']
        print(generator.generator())
        return render_template('form.html', url=url)
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)