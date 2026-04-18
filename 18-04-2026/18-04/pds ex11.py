orders = [
{"order_id":1,"customer":"Rahul","amount":2500},
{"order_id":2,"customer":"Sneha","amount":1800},
{"order_id":3,"customer":"Rahul","amount":3200},
{"order_id":4,"customer":"Amit","amount":1500}
]
totalspend={}
totalorderpercustomer={}
for order in orders:
    cust=order["customer"]
    amt=order["amount"]
    totalspend[cust]=totalspend.get(cust,0)+amt
    totalorderpercustomer[cust]=totalorderpercustomer.get(cust,0)+1
print(totalspend)
maxspend_customer=max(totalspend,key=totalspend.get)
print(maxspend_customer)
print(totalorderpercustomer)
