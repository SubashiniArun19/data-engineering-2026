import csv
orders=[]
with open("orders.csv","r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row["order_id"]=int(row["order_id"])
        row["product_id"]=int(row["product_id"])
        row["quantity"]=int(row["quantity"])
        orders.append(row)
for r in orders:
    print(r)
quant={}
for r in orders:
    if r["product_id"] in quant:
        quant[r["product_id"]]+=r["quantity"]
    else:
        quant[r["product_id"]]=r["quantity"]
print(quant)
orderspercust={}
for r in orders:
    if r["customer"] in orderspercust:
        orderspercust[r["customer"]]+=1
    else:
        orderspercust[r["customer"]]=1
print(orderspercust)