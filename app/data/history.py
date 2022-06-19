import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class History(SqlAlchemyBase):
    __tablename__ = 'history'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    offer_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("offer.offer_id"))
    operation = sqlalchemy.Column(sqlalchemy.String, default="update")
    price = sqlalchemy.Column(sqlalchemy.FLOAT, nullable=True)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now().isoformat())

    offer = orm.relationship("Offer")
