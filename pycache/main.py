from flask import Blueprint,request,jsonify,Response
from flask import current_app
import json
from uuid import uuid4
import traceback
from .cache import cache


main = Blueprint('main',__name__)

@main.route("/")
def index():
    return "Hi from flask-cache 🤓"

@main.route("/cache/new",methods=["POST"])
def update():
    try:
        id = str(uuid4())
        cache.set(id,request.json)
        return jsonify({"status":"SUCCESS","_id":id}),200
    except Exception as e:
        current_app.logger.error(e,traceback.format_exc())
        return jsonify({"status":"ERROR"}),500

@main.route("/cache/<id>")
def get(id):
    try:
        resp = cache.get(id)
        if resp is None:
            return jsonify({"status":"KEY_NOT_IN_CACHE"}),404
        return jsonify(resp),200
    except Exception as e:
        current_app.logger.error(e,traceback.format_exc())
        return jsonify({"status":"ERROR"}),500