from flask import render_template

class Invoice:
    def invoicePage(self):
        return render_template("invoice.html")