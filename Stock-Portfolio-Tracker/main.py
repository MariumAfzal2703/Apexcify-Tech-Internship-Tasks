stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 310
}

stock_name = input("Enter stock symbol (AAPL, TSLA, GOOG, MSFT): ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stock_prices:
    price = stock_prices[stock_name]
    total = price * quantity
    print(f"✅ You invested ${total} in {stock_name}.")

    with open("portfolio.txt", "a") as f:
        f.write(f"{stock_name}, Quantity: {quantity}, Total: ${total}\n")

    print("📁 Investment saved in portfolio.txt")

else:
    print("❌ Stock not found in list.")