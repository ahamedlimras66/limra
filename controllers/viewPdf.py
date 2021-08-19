from flask import send_file

class ViewPdf:
    def show_static_pdf(self):
        with open('sampl1.pdf', 'rb') as static_file:
            print(static_file)
            return send_file(static_file, attachment_filename='bill.pdf')