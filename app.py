from flask import Flask, render_template, request, redirect, flash
from flask_cors import CORS
from url_generator import generator
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(150), unique=True, nullable=False)
    shortened = db.Column(db.String(20), unique=True, nullable=False)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        url = request.form['url-input']
        url_check = Url.query.filter(Url.url == url).first()
        if url_check:
            return render_template('form.html', url=url, shortened= url_check.shortened)
        else:
            random = generator.generator()
            new_url = f'http://localhost:5000/{random}'
            post = Url(url=url, shortened=new_url)
            db.session.add(post)
            db.session.commit()
            return render_template('form.html', url=url, shortened= new_url)
    else:
        return render_template('form.html')

@app.route('/<created_url>')
def getUrl(created_url):
    check = f'http://localhost:5000/{created_url}'
    url_check = Url.query.filter(Url.shortened == check).first()
    if url_check:
        return redirect(url_check.url)
    else:
        flash("Ooops, we don't seem to have that address")
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)