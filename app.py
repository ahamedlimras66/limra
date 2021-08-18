from flask import Flask, url_for

from route.home import home
from route.bill import bill
from route.invoice import invoice

app = Flask(__name__)

app.register_blueprint(home, url_prefix="/")
app.register_blueprint(bill, url_prefix="/bill")
app.register_blueprint(invoice, url_prefix="/invoice")


if __name__ == "__main__":
    app.run(debug=True)