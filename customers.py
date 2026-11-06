# Reflection Questions
# 1. Using bracket notation takes more time to write out and should be used when a key is needed for the code to run. The KeyError message is created as a safeguard. Now on the other hand, the .get() function should be used when the key might not always be missing or it is optional for the code to run. The rule of thumb decision comes down to whether or not the key is needed or optional.
# 2. Exercise 8 runs a code that is similar to how you may organize data in a table in Excel. The Python method is much more useful when dealing with large datasets because the dictionary can hold so much and can be executed with small easy line of code, while Excel rewuires you to write out each dataset.

print("--- Exercise 1 ---")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"]) # accessing value using bracket notation
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

print("--- Exercise 2 ---")
customer["phone"] = "813-555-0142"

print(customer)
customer["tier"] = "platinum"

print(customer)
del customer["email"]

print(customer)

print("--- Exercise 3 ---")

# New Version
print(customer.get("email", "no email on file"))

# Older Version
# try:
#     print(customer["email"])
# except KeyError as error:
#     print(f"KeyError Caught: {error}")

print("--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")

for item in customer:
    print(item)

print("--- Exercise 5 ---")
tier_discounts = {"bronze": 0,
                  "silver": 0.05,
                  "gold": 0.10,
                  "platinum": 0.15}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}") # platinum
print(f"Discount: {discount_rate * 100:.0f}%") # 15%
print(f"Final price: ${final_price:.2f}") # $170.00

print("--- Exercise 6 ---")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate # assuming purchase of $300 for each customer
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} discount on $300 purchase")

print("--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - Only {details['stock']} left in stock!")

print("--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
sales_by_region = {} # empty dictionary to hold sales totals by region
for sale in transactions:
    region = sale["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + sale["amount"]
print(sales_by_region)

for region in sorted(sales_by_region): 
    print(f"{region}: {sales_by_region[region]}")