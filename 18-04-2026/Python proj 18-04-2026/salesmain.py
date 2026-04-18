import csv
sales=[]
with open('sales.csv',"r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row["quantity"]=int(row["quantity"])
        row["price"]=int(row["price"])
        sales.append(row)
total=sum(sale["price"] for sale in sales)
print("TotalRevenue = ",total)
qtyperprod={}
for sale in sales:
    prod=sale["product"]
    if prod in qtyperprod:
        qtyperprod[prod]+=sale["quantity"]
    else:
        qtyperprod[prod]=sale["quantity"]
print("quantity per product")
print(qtyperprod)
revperprod={}
for sale in sales:
    prod=sale["product"]
    if prod in revperprod:
        revperprod[prod]+=sale["price"]
    else:
        revperprod[prod]=sale["price"]
print("revenue per product")
print(revperprod)
for k,v in revperprod.items():
    if v > 50000:
        print(k,v)
print("Product Sales Summary ")
for k,v in qtyperprod.items():
    print(k,"-> Qty :",v,"Revenue :",revperprod[k])
    
