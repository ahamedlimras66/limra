from flask import Flask, url_for

from route.home import home
from route.bill import bill
from route.invoice import invoice
from route.billGenerator import billGenerator
from route.billView import billView

app = Flask(__name__)

app.register_blueprint(home, url_prefix="/")
app.register_blueprint(bill, url_prefix="/bill")
app.register_blueprint(invoice, url_prefix="/invoice")
app.register_blueprint(billGenerator, url_prefix="/billGenerator")
app.register_blueprint(billView, url_prefix="/billView")

if __name__ == "__main__":
    app.run(debug=True)