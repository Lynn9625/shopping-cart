import time
import statistics

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#1 DATA SETUP
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]
#print(products)



#2 INFO INPUTS
#2.1  Captures/ scans product indentifiers and handle invalid inputs
valid_ids = [str(p["id"]) for p in products] 
#print("VALID IDS:", valid_ids)

selected_ids = []

while True:
    selected_id = input("Please input a product identifier, or 'DONE': " ) # the data input will always be a str
    if selected_id == "DONE":
        break
    elif str(selected_id) in valid_ids:
        selected_ids.append(selected_id)
    else:
        print("OH, detected invalid input! Please try again...")
        next 

#print("SELECTED IDS:", selected_ids)



#3 INFO OUTPUTS
#3.1 Displays store info
print("---------------------------------")
print("GREEN FOODS GROCERY")
print("WWW.GREEN-FOODS-GROCERY.COM")
#3.2 Displays checkout date and time
print("---------------------------------")
print("CHECKOUT AT:",time.strftime('%Y-%m-%d %H:%M:%S'))
#3.3 Displays names and prices of all scanned products
print("---------------------------------")
print("SELECTED PRODUCTS:")
for item in products:
    if str(item["id"]) in str(selected_ids):
        price_usd = to_usd(item['price'])
        print(f"...{item['name']}---{price_usd}")
        next
#3.4 Displays tax and totals       
print("---------------------------------")
prices = [x["price"] for x in products if str(x["id"]) in str(selected_ids)]
total_price = sum(prices)
simple_total_price = round(total_price,2)
subtotal = to_usd(simple_total_price)

total_tax = total_price * 0.0875
simple_total_tax = round(total_tax,2)
tax = to_usd(simple_total_tax)

total = to_usd(simple_total_price + simple_total_tax)

print("SUBTOTAL: ",subtotal)
print("TAX: ",tax)
print("TOTAL: ",total)


print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")



##4 CHALLENGE: WRITING RECEIPTS TO FILE
file = open(time.strftime('%Y-%m-%d-%H-%M-%S')+'.txt','w') 
file.write("SELECTED PRODUCTS:")
for item in products:
    if str(item["id"]) in str(selected_ids):
        price_usd = to_usd(item['price'])
        file.write(f"{item['name']}---{price_usd}")
        next
file.write("SUBTOTAL: "+ subtotal)
file.write("TAX: "+ tax)
file.write("TOTAL: " + total)