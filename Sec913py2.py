jls_extract_var = {"name": "Headphones", "price": 150}
Products = [

    {"name": "Laptop", "price": 1000},

    {"name": "Smartphone", "price": 500},

    {"name": "Tablet", "price": 300},
    jls_extract_var


]
 
 # Define range 
min_price = int(input("Enter minimum price: "))
max_price = int(input("Enter maximum price: "))

# Filter products 
filtered_products = [P for P in Products if min_price <= P["price"] <= max_price]

# Sort by price (ascending) 
sorted_products = sorted(filtered_products, key=lambda x: x["price"])

# Display results
for p in sorted_products:
    print(f"{p['name']}: ${p['price']}")


