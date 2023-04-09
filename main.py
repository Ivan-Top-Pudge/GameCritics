from flask import Flask, render_template, redirect
from flask_login import login_user, LoginManager, login_required, logout_user, current_user

from data import db_session
from data.news import News
from data.users import User
from data.games import Game
from data.reviews import Review
from forms.login import LoginForm
from forms.register import RegisterForm
from forms.review_form import ReviewForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'critic_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def home_page():
    return render_template('home_page.html')


@app.route('/news')
def news_list():
    db_sess = db_session.create_session()
    news = db_sess.query(News).all()
    return render_template('news.html', news=news)


@app.route('/games')
def games_list():
    db_sess = db_session.create_session()
    games = db_sess.query(Game).all()
    return render_template('games.html', games=games)


@app.route('/games/<link>', methods=['GET', 'POST'])
def game_info(link: str):
    form = ReviewForm()
    db_sess = db_session.create_session()
    game = db_sess.query(Game).filter(Game.link == link).first()
    reviews = db_sess.query(Review).filter(Review.game_id == game.id)
    if form.validate_on_submit():
        review = Review()
        review.content = form.content.data
        review.author = current_user.id
        review.rate = form.rate.data
        review.game_id = game.id
        db_sess.add(review)
        db_sess.commit()
        return redirect('/')
    return render_template('game_info.html', game=game, reviews=reviews, form=form)


@app.route('/info')
def site_info():
    return render_template('info.html')


@app.route('/top-users')
def top_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).order_by(User.rating).all()
    return render_template('top_users.html', users=users)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="На эту почту уже зарегистрирован аккаунт")
        user = User()
        user.login = form.login.data
        user.name = form.name.data
        user.surname = form.surname.data
        user.email = form.email.data
        user.set_password(form.password.data)

        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.login == form.login.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/profile/<int:user_id>')
def profile(user_id: int):
    db_sess = db_session.create_session()
    user = db_sess.get(User, user_id)
    return render_template('profile.html', user=user)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def add_test_data():
    db_sess = db_session.create_session()
    for i in range(1, 10):
        ...
    db_sess.commit()


if __name__ == '__main__':
    db_session.global_init("db/main.db")
    app.run(port=8080, host='127.0.0.1')
