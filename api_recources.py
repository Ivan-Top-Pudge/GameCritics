from flask import jsonify
from flask_restful import reqparse, abort, Api, Resource

from data import db_session
from data.games import Game
from data.reviews import Review


def abort_if_game_not_found(game_id):
    db_sess = db_session.create_session()
    game = db_sess.get(Game, game_id)
    if not game:
        abort(404, message=f"Game {game_id} not found")


class GameResource(Resource):
    def get(self, game_id):
        abort_if_game_not_found(game_id)
        db_sess = db_session.create_session()
        game = db_sess.query(Game).get(game_id)
        reviews = db_sess.query(Review).filter(Review.game_id == game.id).all()
        avg_rate = round(sum([review.rate for review in reviews if review.rate]) / len(reviews), 1) if reviews else 0
        return jsonify({
            'game': {'title': game.title,
                     'reviews': [{'rate': review.rate, 'user': {'login': review.user.login,
                                                                'rank': review.user.rank,
                                                                'rating': review.user.rating},
                                  'review': review.content} for review in reviews],
                     'developer': game.developer,
                     'description': game.description,
                     'more_info': {'avg_rate': avg_rate, 'reviews_count': len(reviews)}}
        })

    def delete(self, game_id):
        abort_if_game_not_found(game_id)
        db_sess = db_session.create_session()
        game = db_sess.get(Game, game_id)
        db_sess.delete(game)
        db_sess.commit()


class GamesListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        games = db_sess.query(Game).all()
        result = []
        for game in games:
            reviews = db_sess.query(Review).filter(Review.game_id == game.id).all()
            avg_rate = round(sum([review.rate for review in reviews if review.rate]) / len(reviews),
                             1) if reviews else 0
            result.append({'title': game.title, 'developer': game.developer,
                           'reviews_count': len(reviews), 'avg_rate': avg_rate})
        return jsonify({'games': result})
