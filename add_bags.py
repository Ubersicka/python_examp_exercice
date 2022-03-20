price_luggage_over20kg = float(input())
luggage_kg = float(input())
days_till_traveling = int(input())
luggage_count = int(input())

if luggage_kg < 10:
    price_luggage = price_luggage_over20kg * 0.20
elif luggage_kg <= 20:
    price_luggage = price_luggage_over20kg / 2
else:
    price_luggage = price_luggage_over20kg

if days_till_traveling < 7:
    last_price = price_luggage + price_luggage * 0.40
elif days_till_traveling <= 30:
    last_price = price_luggage + price_luggage * 0.15
else:
    last_price = price_luggage + price_luggage * 0.10

print(f"The total price of bags is: {last_price * luggage_count:.2f} lv.")

