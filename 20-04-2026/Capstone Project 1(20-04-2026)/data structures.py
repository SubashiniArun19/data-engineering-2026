from Functions import *
orders = load_orders("orders.csv")
print("Orders (List):", orders)
products_data = load_products("products.json")
product_prices = {}
for pid, details in products_data.items():
    product_prices[pid] = details["price"]
print("Product Prices (Dictionary):", product_prices)
visits = load_visits("website_visits.txt")
unique_visitors = set(visits)
print("Unique Visitors (Set):", unique_visitors)
revenue_tuples = calc_product_revenue(orders, products_data)
print("Revenue Tuples:", revenue_tuples)
customer_spending = calc_customer_spending(orders, products_data)
print("Customer Spending:", customer_spending)
top_customer = find_top_customer(customer_spending)
print("Top Customer:", top_customer)