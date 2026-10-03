
# Mini Data Analysis Tool
# Created by: Om Ahire

sales_data = [
    {"product": "Laptop", "quantity": 2, "price": 50000},
    {"product": "Mouse", "quantity": 10, "price": 500},
    {"product": "Keyboard", "quantity": 5, "price": 1500},
    {"product": "Monitor", "quantity": 3, "price": 12000},
    {"product": "Laptop", "quantity": 1, "price": 50000},
    {"product": "Mouse", "quantity": 8, "price": 500},
]

print("=" * 45)
print("         MINI DATA ANALYSIS TOOL")
print("=" * 45)

# 1. Calculate revenue for each record
total_revenue = 0
product_sales = {}

for item in sales_data:
    revenue = item["quantity"] * item["price"]
    total_revenue += revenue

    product = item["product"]
    product_sales[product] = (
        product_sales.get(product, 0) + revenue
    )

# 2. Calculate key business metrics
total_transactions = len(sales_data)
total_units = sum(item["quantity"] for item in sales_data)
average_transaction = total_revenue / total_transactions

# 3. Identify the top product by revenue
top_product = max(product_sales, key=product_sales.get)

print(f"\nTotal Transactions: {total_transactions}")
print(f"Total Units Sold: {total_units}")
print(f"Total Revenue: Rs. {total_revenue:,.2f}")
print(f"Average Transaction Value: Rs. {average_transaction:,.2f}")

print("\nRevenue by Product:")
for product, revenue in sorted(
    product_sales.items(),
    key=lambda item: item[1],
    reverse=True
):
    print(f"{product}: Rs. {revenue:,.2f}")

print(f"\nTop Product by Revenue: {top_product}")
print("\nAnalysis completed successfully!")