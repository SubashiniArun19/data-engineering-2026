import csv
import json
orders=[]
with open("orders.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row["order_id"]=int(row["order_id"])
        row["product_id"]=int(row["product_id"])
        row["quantity"]=int(row["quantity"])
        orders.append(row)
with open("products.json")as jsonfile:
    data=json.load(jsonfile)
products={}
for product in data["products"]:
    products[product["product_id"]]={
        "name":product["name"],
    "price":product["price"]}
spendpercustomer={}
for o in orders:
    price=products[o["product_id"]]["price"]
    revenue=o["quantity"]*price
    name = o["customer"]
    if name in spendpercustomer:
        spendpercustomer[name]+=revenue
    else:
        spendpercustomer[name]=revenue
print(spendpercustomer)
print("high spend customer")
print(spendpercustomer)
highspendcust=max(spendpercustomer,key=spendpercustomer.get)
print(highspendcust)
print("spending more than 50000")
for s in spendpercustomer:
    if spendpercustomer[s]>50000:
        print(s)
