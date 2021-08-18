from flask import render_template

class Bill:
    def billPage(self):
        return render_template("bill.html")