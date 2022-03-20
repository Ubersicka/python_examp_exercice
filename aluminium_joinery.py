joinery_count = int(input())
type_of_joinery = input()
delivery_type = input()
total_price_joinery = 0

if type_of_joinery == "90X130":
    price = 110
    if joinery_count > 30 and joinery_count <= 60:
        price -= price * 0.05
    elif joinery_count > 60:
        price -= price * 0.08
elif type_of_joinery == "100X150":
    price = 140
    if joinery_count > 40 and joinery_count <= 80:
        price -= price * 0.06
    elif joinery_count > 80:
        price -= price * 0.10
elif type_of_joinery == "130X180":
    price = 190
    if joinery_count > 20 and joinery_count <= 50:
        price -= price * 0.07
    elif joinery_count > 50:
        price -= price * 0.12
elif type_of_joinery == "200X300":
    price = 250
    if joinery_count > 25 and joinery_count <= 50:
        price -= price * 0.09
    elif joinery_count > 50:
        price -= price * 0.14
total_price_joinery = price * joinery_count
if delivery_type == "With delivery":
    total_price_joinery = total_price_joinery + 60
elif delivery_type == "Without delivery":
    pass

if joinery_count > 99:
    discount = total_price_joinery * 0.04
    total_price_joinery = total_price_joinery - discount

if joinery_count < 10:
    print("Invalid order")
else:
    print(f"{total_price_joinery:.2f} BGN")
