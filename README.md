# LIMRA

## Install
```
pipenv shell
pipenv install
python app.py
```

## Database Table
- Customer
    * index (pk, auto increment)
    * customerName 
    (string)
- Product
    * index (PK, auto increment)
    * productName (string)
    * quantity (float)
    * customerID ( customer.index)
## feauter upgrade
- FileName
    * index (PK, auto increment)
    * code