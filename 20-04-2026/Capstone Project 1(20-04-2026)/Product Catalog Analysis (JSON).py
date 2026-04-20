import json
with open("products.json","r") as file:
    data = json.load(file)
products = data["products"]
for p in products:
    print("name: ",p["name"]," price: ",p["price"])
prod={}
for p in products:
    prod[p["product_id"]]={
        "name":p["name"],
        "price":p["price"]
    }
print(prod)
exp=max(products,key=lambda p:p["price"])
print("most expensive product is ",exp)
exp=min(products,key=lambda p:p["price"])
print("least expensive product is ",exp)