from datetime import datetime
import sqlalchemy
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase


class Game(SqlAlchemyBase):
    __tablename__ = 'games'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)
    developer = sqlalchemy.Column(sqlalchemy.String)
    logo = sqlalchemy.Column(sqlalchemy.String)
    likes = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    dislikes = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    created = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now())
    changed = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    link = sqlalchemy.Column(sqlalchemy.String, unique=True)

    approved = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    def __repr__(self):
        return f"<Game> {self.title} by {self.developer}"
