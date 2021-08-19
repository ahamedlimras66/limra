from flask import Blueprint
from controllers.billView import BillView
billView = Blueprint("billView", __name__)

billViewObj = BillView()

billView.add_url_rule("/", view_func=billViewObj.show_static_pdf, methods=['GET'])