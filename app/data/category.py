import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Category(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'category'

    category_id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.FLOAT, nullable=True)
    parent_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("category.category_id"), nullable=True)
    date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())

    def __repr__(self):
        return f"Category: {self.name}"
