import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

print("First 5 Rows")
print(df.head())

print("\nShape")
print(df.shape)

print("\nSummary")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

df["Sales"] = df["Quantity"] * df["Price"]

product_sales = df.groupby("Product")["Sales"].sum()

print("\nSales by Product")
print(product_sales)

category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Category")
print(category_sales)


plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales.png", dpi=300)
plt.show()
plt.close()


quantity = df.groupby("Product")["Quantity"].sum()

plt.figure(figsize=(8, 5))
quantity.plot(kind="bar")
plt.title("Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.tight_layout()
plt.savefig("quantity.png", dpi=300)
plt.show()
plt.close()

print("\nAnalysis completed successfully.")
print("Charts saved as sales.png and quantity.png")