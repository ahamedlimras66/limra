from flask import Blueprint
from model.invoice import Invoice

invoice = Blueprint("invoice", __name__)

invoiceObj = Invoice()

invoice.add_url_rule("/", view_func=invoiceObj.invoicePage, methods=['GET'])