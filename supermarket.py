from datetime import datetime
# Product catalog
products = {
    "Rice": 60,
    "Sugar": 45,
    "Oil": 120,
    "Milk": 30,
    "Biscuits": 20,
    "Soap": 35,
    "Shampoo": 80,
    "Tea": 100,
    "Coffee": 150,
    "Bread": 40
}
cart = {}
print("=" * 50)
print("          BHAVYA SUPERMARKET")
print("             GUNTUR")
print("=" * 50)
# Customer name
customer_name = input("Enter customer name: ")
while True:
    print("\nAvailable Products")
    print("-" * 40)
    for item, price in products.items():
        print(f"{item:<15} ₹{price}")
    print("-" * 40)
    print("Type 'exit' to finish the purchase.")
    print("Type 'view' to view your cart.")
    item = input("Enter product name: ").strip()
    # Exit
    if item.lower() == "exit":
        break
    # View cart
    if item.lower() == "view":
        if not cart:
            print("Your cart is empty.")
        else:
            print("\nYour Cart")
            print("-" * 40)
            for name, quantity in cart.items():
                price = products[name]
                total = price * quantity
                print(f"{name:<15} {quantity:<5} ₹{total}")
        continue
    # Check product
    if item not in products:
        print("Product not found. Please select a product from the list.")
        continue
    # Quantity validation
    while True:
        quantity = input("Enter quantity: ")
        try:
            quantity = int(quantity)
            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    # Add to cart
    if item in cart:
        cart[item] += quantity
    else:
        cart[item] = quantity
    print(f"{quantity} {item}(s) added to your cart.")
# Calculate bill
subtotal = 0
print("\n")
print("=" * 60)
print("                  FINAL RECEIPT")
print("              BHAVYA SUPERMARKET")
print("                    GUNTUR")
print("=" * 60)
print(f"Customer Name : {customer_name}")
print(f"Date & Time   : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
print("-" * 60)
print(f"{'Item':<15}{'Qty':<8}{'Price':<12}{'Total':<12}")
print("-" * 60)
for item, quantity in cart.items():

    price = products[item]
    item_total = price * quantity
    subtotal += item_total
    print(
        f"{item:<15}"
        f"{quantity:<8}"
        f"₹{price:<11}"
        f"₹{item_total:<11}"
    )
# Tax
tax = subtotal * 0.12
grand_total = subtotal + tax
print("-" * 60)
print(f"{'Subtotal':<35} ₹{subtotal:.2f}")
print(f"{'Tax (12%)':<35} ₹{tax:.2f}")
print(f"{'Grand Total':<35} ₹{grand_total:.2f}")
print("=" * 60)
print("             Thank you for shopping!")
print("                  Visit Again!")
print("=" * 60)