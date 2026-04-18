import json
with open('orders.json') as file:
    data= json.load(file)
orders=data['orders']
print(orders)
totalrevenue=sum(o["amount"] for o in orders)
print(totalrevenue)
cus_spend={}
for o in orders:
    cus=o["customer"]
    amt=o["amount"]
    cus_spend[cus]=cus_spend.get(cus,0)+amt
print(cus_spend)
highestspendcus=max(cus_spend,key=cus_spend.get)
print(highestspendcus)
total_order ={}
for o in orders:
    cus=o["customer"]
    total_order[cus]=total_order.get(cus,0)+1
print(total_order)