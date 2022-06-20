"""Модель таблицы category с данными о категориях"""

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

    def get_info(self):
        return {
            "type": "CATEGORY",
            "name": self.name,
            "id": self.category_id,
            "parentId": self.parent_id,
            "price": int(self.price),
            "date": f"{self.date.isoformat()}.{str(self.date.microsecond).zfill(3)}Z",
            "childrens": []
        }

    def __repr__(self):
        return f"Category: {self.name}"
