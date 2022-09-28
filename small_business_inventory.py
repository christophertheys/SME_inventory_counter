# SME inventory

# This program will be used to calculate the necessary prices of required stock in a café.

print("Stock valuation for Cafe".upper(), "\n")

menu_list = ["Sugar sachets", "Bags of coffee beans for the filters", "Bread rolls", "Newspapers"]
int_stock_dict = {"Sugar sachets": 65,
                  "Bags of coffee beans for the filters": 5,
                  "Bread rolls": 10,
                  "Newspapers": 15}
int_price_of_stock = {"Sugar sachets": 0.5,
                      "Bags of coffee beans for the filters": 250,
                      "Bread rolls": 5,
                      "Newspapers": 2}

# The calculation of the stock will be taken from the two dictionaries listed above

print("\t \t \t Total value of stock: \n")
print(menu_list[0], int_stock_dict["Sugar sachets"] * int_price_of_stock["Sugar sachets"],
      "\n", menu_list[1], int_stock_dict["Bags of coffee beans for the filters"]
      * int_price_of_stock["Bags of coffee beans for the filters"], "\n", menu_list[2],
      int_stock_dict["Bread rolls"] * int_price_of_stock["Bread rolls"], "\n", menu_list[3],
      int_stock_dict["Newspapers"] * int_price_of_stock["Newspapers"], "\n")
