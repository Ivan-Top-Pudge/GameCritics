from flask import Flask, render_template

from data import db_session
from data.news import News
from data.users import User
from data.games import Game
from data.reviews import Review

app = Flask(__name__)


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


@app.route('/games/<link>')
def game_info(link: str):
    db_sess = db_session.create_session()
    game = db_sess.query(Game).filter(Game.link == link).first()
    reviews = db_sess.query(Review).filter(Review.game_id == game.id)
    return render_template('game_info.html', game=game, reviews=reviews)


@app.route('/info')
def site_info():
    return render_template('info.html')


@app.route('/top-users')
def top_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).order_by(User.rating).all()
    return render_template('top_users.html', users=users)


def add_test_data():
    db_sess = db_session.create_session()
    for i in range(1, 10):
        ...
    db_sess.commit()


if __name__ == '__main__':
    db_session.global_init("db/main.db")
    app.run(port=8080, host='127.0.0.1')
