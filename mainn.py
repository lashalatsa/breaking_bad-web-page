from flask import Flask, redirect, url_for, render_template, request, session,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Python'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///film.sqlite'
app.config['SQLALCHEMY_BINDS'] = {'first':'sqlite:///quotes.sqlite'}
db = SQLAlchemy(app)

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    birthday = db.Column(db.FLOAT(12), nullable=False)
    name = db.Column(db.String(40), nullable=False)
    nickname = db.Column(db.String(40), nullable=False)
    portrayed = db.Column(db.String(40), nullable=False)
    status = db.Column(db.String(40), nullable=False)

    def __str__(self):
        return f'{self.id}) დაბადების თარიღია:{self.birthday}; სახელია: {self.name}; მეტსახელია: {self.nickname}; ნამდვილი სახელია : {self.portrayed}; სტატუსია:{self.status}'

class Quotes(db.Model):
    __bind_key__ = 'first'
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String(70), nullable=False)
    author = db.Column(db.String(30), nullable=False)

    def __str__(self):
        return f'{self.id})ციტატა:{self.quote}; ავტორი:{self.author}'


#
#
# b1 = Quotes.query.all()                                                                ##ერთი ჩანაწერი
# print(b1)
#
# all_quotes = Quotes.query.all()                                                          ##ყველა ჩანაწერი
# # all_books = Books.query.filter_by(author='აკაკი წერეთელი').all()
# for each in all_quotes:
#     print(each)


#

@app.route('/')
def home():
    all_film =  Film.query.all()
    return render_template('index.html', all_film=all_film)


@app.route('/user')
def user():
    all_quotes = Quotes.query.all()
    return render_template('user.html', all_quotes=all_quotes)



@app.route('/login')
def login():
    return render_template('login.html')



@app.route('/books')
def books():
    return render_template('books.html')



if __name__ == "__main__":
    app.run(debug=True)
