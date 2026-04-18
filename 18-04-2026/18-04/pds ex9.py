sales = [
{"product":"Laptop","qty":5},
{"product":"Mouse","qty":20},
{"product":"Laptop","qty":3},
{"product":"Keyboard","qty":10}
]
total_sales = {}

for sale in sales:
    prod=sale["product"]
    qty=sale["qty"]
    total_sales[prod]=total_sales.get(prod,0)+qty
print(total_sales)
highest_sold_product=max(total_sales,key=total_sales.get)
print(highest_sold_product)