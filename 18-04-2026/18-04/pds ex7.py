products = {
"Laptop":75000,
"Mobile":30000,
"Tablet":25000
}
for prod,price in products.items():
    products[prod]=price+(price*(0.1))
print(products)