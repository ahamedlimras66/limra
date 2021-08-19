from flask.globals import request
from model.makePDF import MakePDF
import json

class BillGenerator:
    def bill(self, jsdata):
        billObj = MakePDF(
            itemX=50,
            y=660,
            quantityX=480,
            ySpace=12
        )
        billObj.content(jsdata)
        billObj.write("sampl1")
    
    def invoice(self, jsdata):
        pass

    def filterBy(self):
        generatorType = request.args.get("type")
        jsdata = json.loads(request.args.get("data"))
        if generatorType == "1":
            self.bill(jsdata)
        elif generatorType == "2":
            self.invoice(jsdata)
        return {"status": "generated"}