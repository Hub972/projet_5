###### **_Project_ 5**__

This project use the API OpenFoodFacts and this data base for help the user to found a product better than her own 
product present in the local data base.The User can choose to change or not  the product in the data base and
display a list of substituted products.In the 'db' package you can run the db_main for create and load the data
base with some products, just change this 'from .db_engine import sql, Products, con, trans' in this 
'from db_engine import sql, Products, con, trans' in db.db_interaction.Don't forget back in the first configuration for
run the 'main.py'. The script make with Python3.7, requests 2.21.0, sqlalchemy 1.2.18. 
Use pip install -r requirements.txt to install the dependency.