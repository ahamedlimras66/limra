from flask import Blueprint
from model.bill import Bill

bill = Blueprint("bill", __name__)

billObj = Bill()

bill.add_url_rule("/", view_func=billObj.billPage, methods=['GET'])