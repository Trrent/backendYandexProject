from flask import Blueprint, request, jsonify
from flask_restful import abort

from . import db_session
from .offer import Offer
from .category import Category
from .history import History
from .functions import validate_iso8601, get_date

blueprint = Blueprint(
    'items_api',
    __name__,
    template_folder='templates'
)


@blueprint.errorhandler(400)
def unauthorized(error):
    response = jsonify({
        "code": 400,
        "message": "Validation Failed"
    })
    response.status_code = 400
    return response


@blueprint.route('/imports', methods=['POST'])
def imports():
    data = request.json
    if not data:
        abort(400)
    if not data["updateDate"]:
        abort(400)
    if not validate_iso8601(data["updateDate"]):
        abort(400)
    session = db_session.create_session()
    try:
        date = get_date(data["updateDate"])
        for item in request.json["items"]:
            if item["type"] == "CATEGORY":
                it = session.query(Category).filter(Category.category_id == item["id"]).first()
                if not it:
                    it = Category(category_id=item["id"],
                                  name=item["name"],
                                  parent_id=item["parentId"],
                                  date=date)
                    session.add(it)
                else:
                    it.name = item["name"]
                    it.parent_id = item["parentId"]
                    it.date = date
                session.commit()
            elif item["type"] == "OFFER":
                it = session.query(Offer).filter(Offer.offer_id == item["id"]).first()
                if not it:
                    it = Offer(offer_id=item["id"],
                               name=item["name"],
                               price=item["price"],
                               parent_id=item["parentId"],
                               date=date)
                    session.add(it)
                else:
                    it.name = item["name"]
                    it.parent_id = item["parentId"]
                    it.date = date
                add_history_record(item["id"], item["price"], date)
                session.commit()
            else:
                abort(400)
        update_category_price()
        return jsonify({'success': 'OK'})
    except Exception as e:
        print(e)
        abort(400)


@blueprint.route('/api/nodes')
def get_nodes():
    return "Обработчик в items_api"


def add_history_record(offer_id, price, date):
    session = db_session.create_session()
    offer = session.query(Offer).filter(Offer.offer_id == offer_id).first()
    history = History(offer_id=offer_id, price=price, modified_date=date)
    if offer:
        history.operation = 'modified' if offer.price != price else 'update'
    else:
        history.operation = 'modified'
    session.add(history)
    session.commit()


def update_category_price():
    def update_price(parent_id=None):
        categories = session.query(Category).filter(Category.parent_id == parent_id).all()
        category_price, category_count = 0, 0
        for category in categories:
            price, count = 0, 0
            subcategories = session.query(Category).filter(Category.parent_id == category.category_id).all()
            if subcategories:
                f = update_price(parent_id=category.category_id)
                price, count = price + f[0], f[1]
            offers = session.query(Offer).filter(Offer.parent_id == category.category_id).all()
            for offer in offers:
                price += offer.price
                count += 1
            category.price = price // count
            session.commit()
            category_price, category_count = category_price + price, category_count + count
        return category_price, category_count

    session = db_session.create_session()
    update_price()
