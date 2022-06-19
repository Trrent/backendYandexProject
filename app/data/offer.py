import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Offer(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'offer'

    offer_id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.FLOAT)
    parent_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("category.category_id"), nullable=True)
    date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now().isoformat())

    def get_info(self):
        return {"type": "OFFER",
                "name": self.name,
                "id": self.offer_id,
                "parentId": self.parent_id,
                "price": self.price,
                "date": self.date.isoformat(),
                "childrens": None,
                }

    def __repr__(self):
        return f"Offer: {self.name}"
