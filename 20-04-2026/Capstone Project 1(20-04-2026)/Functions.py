import csv
import json


def load_visits(filename):
    with open(filename,"r") as file:
        return file.read().splitlines()
def load_products(filename):
    with open(filename,"r") as file:
        data=json.load(file)
    products={}
    for p in data["products"]:
        products[p["product_id"]]={"name":p["name"],"price":p["price"]}
    return products
def load_orders(filename):
    orders=[]
    with open(filename,"r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["order_id"] = int(row["order_id"])
            row["product_id"] = int(row["product_id"])
            row["quantity"] = int(row["quantity"])
            orders.append(row)
    return orders
def calc_product_revenue(orders, products):
    rev = {}
    for o in orders:
        pid = o["product_id"]
        price = products[pid]["price"]
        revenue = o["quantity"] * price
        if pid in rev:
            rev[pid]["revenue"] += revenue
        else:
            rev[pid] = {
                "name": products[pid]["name"],
                "revenue": revenue}
    return rev
def calc_customer_spending(orders, products):
    spending = {}
    for o in orders:
        customer = o["customer"]
        price = products[o["product_id"]]["price"]
        revenue = o["quantity"] * price
        if customer in spending:
            spending[customer] += revenue
        else:
            spending[customer] = revenue
    return spending
def find_top_customer(spending):
    top = max(spending, key=spending.get)
    return top, spending[top]



