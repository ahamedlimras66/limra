from PyPDF2 import PdfFileWriter, PdfFileReader
import io, os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

"""
item - (100, 600)
quantity - (480, 600)
"""
class MakePDF:
    def __init__(self, itemX, y, quantityX, ySpace) -> None:
        self.existing_pdf = PdfFileReader(open("LIMRA.pdf", "rb"))
        self.itemX = itemX
        self.y = y
        self.quantityX = quantityX
        self.ySpace = ySpace
    
    def changePosition(self):
        self.y = self.y - self.ySpace
        self.y = self.y - self.ySpace
    
    def content(self, data=None):
        self.packet = io.BytesIO()
        # create a new PDF with Reportlab
        can = canvas.Canvas(self.packet, pagesize=letter)
        for row in data["productInfo"]:
            can.drawString(self.itemX, self.y, row["item"])
            can.drawString(self.quantityX, self.y, row["quantity"])
            self.changePosition()
        can.save()
    
    def write(self, fileName):
        self.packet.seek(0)
        new_pdf = PdfFileReader(self.packet)
        output = PdfFileWriter()
        page = self.existing_pdf.getPage(0)
        output.addPage(page)

        # finally, write "output" to a real file
        outputStream = open(fileName+".pdf", "wb")
        output.write(outputStream)

        page = self.existing_pdf.getPage(1)
        output.addPage(page)
        page.mergePage(new_pdf.getPage(0))
        output.write(outputStream)
        outputStream.close()