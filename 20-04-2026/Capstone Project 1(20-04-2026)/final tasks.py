from Functions import  *
visits = load_visits("website_visits.txt")
orders = load_orders("orders.csv")
visitor_set = set(visits)
customer_set = set(o["customer"] for o in orders)
no_orders = visitor_set - customer_set
print("Visitors who never ordered:")
print(no_orders)