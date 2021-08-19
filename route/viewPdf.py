from flask import Blueprint
from controllers.viewPdf import ViewPdf
viewPdf = Blueprint("viewPdf", __name__)

viewPdfObj = ViewPdf()

viewPdf.add_url_rule("/", view_func=viewPdfObj.show_static_pdf, methods=['GET'])