import csv

total_revenue = 0
customer_spending = {}
category_revenue = {}
city_revenue = {}
daily_revenue = {}

with open("data/orders.csv", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        customer = row["customer"]
        category = row["category"]
        city = row["city"]
        date = row["date"]
        amount = float(row["amount"])

        # totale globale
        total_revenue += amount

        # per cliente
        customer_spending[customer] = customer_spending.get(customer, 0) + amount

        # per categoria
        category_revenue[category] = category_revenue.get(category, 0) + amount

        # per città
        city_revenue[city] = city_revenue.get(city, 0) + amount

        # per data
        daily_revenue[date] = daily_revenue.get(date, 0) + amount

# risultati principali
best_customer = max(customer_spending, key=customer_spending.get)
best_category = max(category_revenue, key=category_revenue.get)
best_city = max(city_revenue, key=city_revenue.get)

print(f"Total revenue: €{total_revenue:.2f}")
print(f"Best customer: {best_customer}")
print(f"Best category: {best_category}")
print(f"Top city: {best_city}")

print("\nRevenue by city:")
for city, value in city_revenue.items():
    print(f"- {city}: €{value:.2f}")

print("\nRevenue by day:")
for date, value in daily_revenue.items():
    print(f"- {date}: €{value:.2f}")
