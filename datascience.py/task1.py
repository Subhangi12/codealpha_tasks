# Unemployment Analysis using Pure Python (No Libraries)

# Sample unemployment data (Year-Month, Rate)
dates = [
    "2019-01","2019-02","2019-03","2019-04","2019-05","2019-06",
    "2019-07","2019-08","2019-09","2019-10","2019-11","2019-12",
    "2020-01","2020-02","2020-03","2020-04","2020-05","2020-06",
    "2020-07","2020-08","2020-09","2020-10","2020-11","2020-12",
    "2021-01","2021-02","2021-03","2021-04","2021-05","2021-06",
    "2021-07","2021-08","2021-09","2021-10","2021-11","2021-12"
]

unemployment_rate = [
    6.5,6.4,6.6,6.7,6.8,6.9,
    7.0,7.1,7.0,6.9,6.8,6.7,
    7.5,8.2,9.1,10.3,9.8,9.2,
    8.7,8.1,7.6,7.2,6.9,6.8,
    6.7,6.6,6.5,6.4,6.3,6.2,
    6.1,6.0,5.9,5.8,5.7,5.6
]

# Basic statistics
highest = max(unemployment_rate)
lowest = min(unemployment_rate)
average = sum(unemployment_rate) / len(unemployment_rate)

print("Highest Unemployment Rate:", highest)
print("Lowest Unemployment Rate:", lowest)
print("Average Unemployment Rate:", round(average, 2))

# COVID-19 impact analysis
print("\nCOVID-19 Impact (2020):")
for i in range(len(dates)):
    if dates[i].startswith("2020"):
        print(dates[i], ":", unemployment_rate[i], "%")

# Seasonal trend (monthly average)
monthly_data = {}

for i in range(len(dates)):
    month = dates[i].split("-")[1]
    if month not in monthly_data:
        monthly_data[month] = []
    monthly_data[month].append(unemployment_rate[i])

print("\nSeasonal Trends (Average by Month):")
for month in sorted(monthly_data):
    avg = sum(monthly_data[month]) / len(monthly_data[month])
    print("Month", month, ":", round(avg, 2), "%")

# Trend direction
if unemployment_rate[-1] < unemployment_rate[0]:
    print("\nOverall Trend: Unemployment Decreased Over Time")
else:
    print("\nOverall Trend: Unemployment Increased Over Time")