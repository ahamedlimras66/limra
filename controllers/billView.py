from flask import send_file

class BillView:
    def show_static_pdf(self):
        return send_file(open('sampl1.pdf', 'rb'), attachment_filename='bill.pdf')