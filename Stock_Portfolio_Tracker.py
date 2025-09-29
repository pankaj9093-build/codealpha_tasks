stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 300
}

print("Welcome to the Stock Portfolio Tracker!")
print("Here are the available stocks you can choose from:")
print(", ".join(stock_prices.keys()))

try:
    num_stocks = int(input("\nHow many different stocks would you like to enter? "))
except ValueError:
    print("Oops! That's not a valid number. Exiting...")
    exit()
portfolio = {}
total_value = 0

for i in range(num_stocks):
    print(f"\nStock {i + 1} of {num_stocks}")
    symbol = input("Enter the stock symbol (e.g., AAPL): ").upper()

    if symbol not in stock_prices:
        print(f"Sorry, {symbol} is not in the available stock list. Skipping.")
        continue

    try:
        qty = int(input(f"How many shares of {symbol} do you own? "))
    except ValueError:
        print("That wasn't a valid number. Skipping this stock.")
        continue

    price = stock_prices[symbol]
    value = price * qty

    portfolio[symbol] = {
        "quantity": qty,
        "price": price,
        "value": value
    }

    total_value += value

print("\nYour Stock Portfolio Summary:")
print("------------------------------")

if not portfolio:
    print("You didn't enter any valid stocks.")
else:
    for symbol, data in portfolio.items():
        print(f"{symbol}: {data['quantity']} shares x ${data['price']} = ${data['value']}")

    print(f"\nTotal Investment Value: ${total_value}")
save = input("\nWould you like to save this summary to a file? (yes/no): ").strip().lower()

if save == "yes":
    file_name = "portfolio_summary.txt"
    with open(file_name, "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("------------------------\n")
        for symbol, data in portfolio.items():
            file.write(f"{symbol}: {data['quantity']} shares x ${data['price']} = ${data['value']}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")
    print(f"Summary saved to '{file_name}'.")
else:
    print("Okay, not saving the summary.")

print("\nThanks for using the Stock Portfolio Tracker! Goodbye! ")

