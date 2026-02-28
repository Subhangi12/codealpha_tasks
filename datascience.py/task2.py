# Sales Prediction using Pure Python (No Libraries)

# Sample sales data
advertising_spend = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500]
sales = [12000, 18000, 23000, 28000, 34000, 39000, 45000, 50000]

# Basic statistics
highest_sales = max(sales)
lowest_sales = min(sales)
average_sales = sum(sales) / len(sales)

print("Highest Sales:", highest_sales)
print("Lowest Sales:", lowest_sales)
print("Average Sales:", round(average_sales, 2))

# Simple linear prediction logic
# Calculate average increase in sales per unit advertising spend
sales_change = []
spend_change = []

for i in range(1, len(sales)):
    sales_change.append(sales[i] - sales[i-1])
    spend_change.append(advertising_spend[i] - advertising_spend[i-1])

avg_sales_increase = sum(sales_change) / sum(spend_change)

# Predict future sales
future_ad_spend = 5000
predicted_sales = sales[-1] + avg_sales_increase * (future_ad_spend - advertising_spend[-1])

print("\nFuture Advertising Spend:", future_ad_spend)
print("Predicted Sales:", round(predicted_sales, 2))

# Impact of advertising on sales
print("\nImpact of Advertising on Sales:")
for i in range(len(advertising_spend)):
    print("Ad Spend:", advertising_spend[i], "→ Sales:", sales[i])

# Business insight
if avg_sales_increase > 0:
    print("\nInsight: Increasing advertising spend leads to higher sales.")
else:
    print("\nInsight: Advertising spend has limited impact on sales.")