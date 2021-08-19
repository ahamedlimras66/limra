from flask import Blueprint
from controllers.billGenerator import BillGenerator

billGenerator = Blueprint("billGenerator", __name__)

billGeneratorObj = BillGenerator()

billGenerator.add_url_rule("/<jsdata>/", view_func=billGeneratorObj.filterBy, methods=['POST'])