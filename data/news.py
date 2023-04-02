from datetime import datetime
import sqlalchemy
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase


class News(SqlAlchemyBase):
    __tablename__ = 'news'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    content = sqlalchemy.Column(sqlalchemy.String)
    author = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    likes = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    dislikes = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now())
    changed = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    official = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    user = orm.relationship('User')

    def __repr__(self):
        return f"<News> {self.title} by {self.author}"
