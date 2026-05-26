original_pricings = {"TCL 85 Inch": "price=$1,200", 
            "Samsung 98-Inch": "price=$2,900", 
            "Hisense 100": "price=$3,100"}
updated_pricings = {"TCL 85 Inch": "price=$2,990"}
original_pricings.update(updated_pricings)
print(original_pricings.keys())
user_input = int(input("Which TV are you looking to know the price of? The first, second, or third? Enter 1, 2, or 3."))
if user_input not in [1, 2, 3]:
    print("Invalid input. Select 1, 2, or 3.")
if user_input == 1:
    print(f"The price of the item you selected 'TCL 85 Inch' is {updated_pricings['TCL 85 Inch'][6:]}")
if user_input == 2:
    print(f"The price of the item you selected 'Samsung 98-Inch' is {original_pricings['Samsung 98-Inch'][6:]}")
if user_input == 3:
    print(f"The price of the item you selected 'Hisense 100' is {original_pricings['Hisense 100'][6:]}")