import json
import csv
from ftplib import print_line

orders=[]
with open("orders.csv","r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row["order_id"]=int(row["order_id"])
        row["product_id"]=int(row["product_id"])
        row["quantity"]=int(row["quantity"])
        orders.append(row)
with open("products.json","r") as file:
    data = json.load(file)
products={}
for product in data["products"]:
    products[product["product_id"]]={
        "name":product["name"],
    "price":product["price"]}
print(products)
revperorder={}
print("Revenue per order")
for o in orders:
    price=products[o["product_id"]]["price"]
    revenue=o["quantity"]*price
    revperorder[o["order_id"]]=revenue
print(revperorder)
print("Total Revenue")
totrev=sum(revperorder.values())
print(totrev)
revperprod={}
for o in orders:
    price=products[o["product_id"]]["price"]
    revenue=o["quantity"]*price
    if o["product_id"] in revperprod:
        revperprod[o["product_id"]]["revenue"]+=revenue
    else:
        name=products[o["product_id"]]["name"]
        revperprod[o["product_id"]]={"name":name,"revenue":revenue}
print(revperprod)
for name,rev in revperprod.items():
    print (rev["name"],":",rev["revenue"])
highsellprod=max(revperprod,key=lambda x:revperprod[x]["revenue"] )
print(revperprod[highsellprod]["name"])



